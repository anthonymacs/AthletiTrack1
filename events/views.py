# events/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.db import transaction
from django.forms import formset_factory
from django import forms
from django.db.models import Q 

from .models import Event, Coach
from .forms import EventForm, ParticipantManagementForm, EventScheduleForm, GameReportForm, EventOutcomeForm
from users.models import CustomUser
from athletes.models import Athlete, PerformanceStat
#from athletes.forms import BulkFilterForm
from core.models import Sport, Campus, Team, Statistic
from athletes.forms import TeamSelectForm


@login_required
def event_list(request):
    """
    Displays a list of events, scoped to the user's role.
    - Admins see all events.
    - Coaches see events relevant to their team.
    - Athletes see events they are participating in.
    """
    user = request.user
    
    # --- THIS IS THE NEW PERMISSION-BASED QUERYSET LOGIC ---
    if user.role == CustomUser.Role.ADMINISTRATOR:
        # Admins see all events.
        queryset = Event.objects.all()
        
    elif user.role == CustomUser.Role.COACH:
        # Coaches see events where at least one participant is from their team.
        if hasattr(user, 'coach') and user.coach.team:
            coachs_team = user.coach.team
            queryset = Event.objects.filter(participants__team=coachs_team).distinct()
        else:
            queryset = Event.objects.none() # A coach with no team sees no events.
            
    elif user.role == CustomUser.Role.ATHLETE:
        # Athletes see only the events they are registered for.
        if hasattr(user, 'athlete'):
            queryset = user.athlete.attended_events.all()
        else:
            queryset = Event.objects.none() # An athlete with no profile sees no events.
    
    else:
        # Default for any other unforeseen role is to see nothing.
        queryset = Event.objects.none()
    # --- END OF NEW LOGIC ---

    # We order the final, filtered queryset by the start time.
    events = queryset.select_related('coach_in_charge__user').order_by('start_time')

    context = {
        'events': events,
    }
    return render(request, 'events/event_list.html', context)


@login_required
def event_detail(request, pk):
    """
    Displays details for a single event and handles the form for managing
    participants, with filtering by Team.
    """
    # Use select_related for efficiency
    event = get_object_or_404(Event.objects.select_related('coach_in_charge__user'), pk=pk)
    #participants = event.participants.all().select_related('user', 'team')

    # --- UPDATED Query and Filtering Logic ---
    # The base query for the form now uses the team relationship
    athlete_list = Athlete.objects.all().select_related('user', 'team')
    team_filter = request.GET.get('team')

    if team_filter:
        athlete_list = athlete_list.filter(team_id=team_filter)
    # --- END OF UPDATES ---

    # Initialize the form
    participant_form = ParticipantManagementForm(instance=event)
    participant_form.fields['participants'].queryset = athlete_list

    if request.method == 'POST':
        # This POST is only for updating the participant list
        if 'update_participants' in request.POST:
            if request.user.role in [CustomUser.Role.COACH, CustomUser.Role.ADMINISTRATOR]:
                form = ParticipantManagementForm(request.POST, instance=event)
                form.fields['participants'].queryset = athlete_list
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Participant list updated successfully.')
                    return redirect('event-detail', pk=event.pk)

    context = {
        'event': event,
        'participants': event.participants.all().select_related('user'),
        'participant_form': participant_form,
        'all_teams': Team.objects.all().order_by('sport__name'),
    }
    return render(request, 'events/event_detail.html', context)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventScheduleForm # Use the new form with start/end time
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event-list')

    def test_func(self):
        return self.request.user.role in [CustomUser.Role.COACH, CustomUser.Role.ADMINISTRATOR]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = "Edit Event"
        return context


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # --- THIS CONTENT NEEDS TO BE INDENTED ---
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event-list')

    def test_func(self):
        return self.request.user.role in [CustomUser.Role.COACH, CustomUser.Role.ADMINISTRATOR]
    # --- END OF INDENTED BLOCK ---


# The next view should start with no indentation
@login_required
def schedule_events_view(request):
    """
    Handles a two-step process for scheduling multiple events for a specific Team.
    1. User selects a Team.
    2. User fills out details for one or more events. The system then automatically
       adds all athletes from the selected Team as participants and assigns the
       Team's coach as the one in charge.
    """
    team_id = request.GET.get('team')
    show_formset = False
    team = None
    filter_form = None
    formset = None

    EventFormSet = formset_factory(EventScheduleForm, extra=1)

    # Step 1: Check if a team has been selected from the URL
    if team_id:
        try:
            team = Team.objects.select_related('coach').get(pk=team_id)
            show_formset = True
        except Team.DoesNotExist:
            messages.error(request, "Invalid Team selected.")
            return redirect('event-schedule') # Redirect back to the filter page

    # Step 2: Handle the POST request from the formset
    if request.method == 'POST' and show_formset:
        formset = EventFormSet(request.POST)
        if formset.is_valid():
            # Get all athletes that belong to the selected team
            filtered_athletes = Athlete.objects.filter(team=team)
            try:
                with transaction.atomic():
                    created_events_count = 0
                    for form in formset:
                        if form.has_changed():
                            event = form.save(commit=False)
                            # Automatically assign the team's designated coach as the one in charge
                            if hasattr(team, 'coach'):
                                event.coach_in_charge = team.coach
                            event.save()
                            # Automatically add all athletes from the team as participants
                            event.participants.set(filtered_athletes)
                            created_events_count += 1

                if created_events_count > 0:
                    messages.success(request, f"Successfully scheduled {created_events_count} event(s) for team '{team}'.")
                return redirect('event-list')
            except Exception as e:
                messages.error(request, f'An error occurred: {e}')
    # Handle GET requests for either Step 1 or Step 2
    else:
        if show_formset:
            formset = EventFormSet()
        else:
            filter_form = TeamSelectForm()

    context = {
        'filter_form': filter_form,
        'formset': formset,
        'selected_team': team,
        'show_formset': show_formset,
    }
    return render(request, 'events/event_schedule_form.html', context)


# events/views.py

@login_required
def game_report_view(request, pk):
    """
    Handles the "Game Report" page:
    1. EventOutcomeForm - final score and Win/Loss.
    2. GameReportForms - player statistics.
    """
    event = get_object_or_404(Event.objects.select_related('coach_in_charge__user'), pk=pk)
    
    # --- Authorization ---
    is_in_charge = hasattr(request.user, 'coach') and request.user.coach == event.coach_in_charge
    is_admin = request.user.role == CustomUser.Role.ADMINISTRATOR
    if not (is_in_charge or is_admin):
        messages.error(request, "You are not authorized to manage stats for this event.")
        return redirect('event-detail', pk=event.pk)

    sport = event.participants.first().team.sport if event.participants.exists() else None

    if request.method == 'POST':
        # --- Form 1: Handle Event Outcome Submission ---
        if 'save_outcome' in request.POST:
            outcome_form = EventOutcomeForm(request.POST, instance=event)
            if outcome_form.is_valid():
                outcome_form.save()
                our_score = outcome_form.cleaned_data.get('our_score')
                opponent_score = outcome_form.cleaned_data.get('opponent_score')

                if sport and our_score is not None and opponent_score is not None:
                    try:
                        win_stat_obj, _ = Statistic.objects.get_or_create(
                            sport__isnull=True, short_name='wins', defaults={'name': 'Wins'}
                        )
                        loss_stat_obj, _ = Statistic.objects.get_or_create(
                            sport__isnull=True, short_name='losses', defaults={'name': 'Losses'}
                        )

                        result_stat = None
                        stat_to_remove = None

                        if our_score > opponent_score:
                            result_stat = win_stat_obj
                            stat_to_remove = loss_stat_obj
                        elif our_score < opponent_score:
                            result_stat = loss_stat_obj
                            stat_to_remove = win_stat_obj

                        if result_stat:
                            with transaction.atomic():
                                for athlete in event.participants.all():
                                    if stat_to_remove:
                                        PerformanceStat.objects.filter(
                                            athlete=athlete, statistic=stat_to_remove, event=event
                                        ).delete()
                                    PerformanceStat.objects.update_or_create(
                                        athlete=athlete, statistic=result_stat, event=event,
                                        defaults={'value': '1'}
                                    )
                    except Exception as e:
                        messages.warning(request, "Please define 'wins' and 'losses' as universal stats in settings.")

                messages.success(request, "Event outcome saved successfully.")
            else:
                messages.error(request, "Invalid score entered. Please try again.")
            return redirect('game-report', pk=event.pk)

        # --- Form 2: Handle Player Statistics Submission ---
        elif 'save_player_stats' in request.POST:
            all_stats_for_sport = Statistic.objects.filter(Q(sport__isnull=True) | Q(sport=sport))
            for athlete in event.participants.all():
                form = GameReportForm(request.POST, sport=sport, prefix=f'athlete_{athlete.pk}')
                if form.is_valid():
                    for stat_definition in all_stats_for_sport:
                        value = form.cleaned_data.get(stat_definition.short_name)
                        if value is not None and str(value).strip() != '':
                            PerformanceStat.objects.update_or_create(
                                athlete=athlete, statistic=stat_definition, event=event,
                                defaults={'value': str(value).strip()}
                            )
            messages.success(request, f"Player stats for '{event.name}' updated successfully.")
            return redirect('game-report', pk=event.pk)

    # --- GET Request Logic ---
    outcome_form = EventOutcomeForm(instance=event)
    participant_forms = {}
    if sport:
        for athlete in event.participants.all():
            existing_stats = PerformanceStat.objects.filter(athlete=athlete, event=event)
            initial_data = {stat.statistic.short_name: stat.value for stat in existing_stats}
            participant_forms[athlete.pk] = GameReportForm(initial=initial_data, sport=sport, prefix=f'athlete_{athlete.pk}')

    context = {
        'event': event,
        'outcome_form': outcome_form,
        'participants': event.participants.all().select_related('user'),
        'participant_forms': participant_forms,
        'first_form': list(participant_forms.values())[0] if participant_forms else None,
    }
    return render(request, 'events/game_report.html', context)
