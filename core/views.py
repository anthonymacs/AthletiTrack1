# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from athletes.models import Athlete #, CustomUser
from events.models import Event
from .models import Feedback, Team
from .forms import FeedbackForm, TeamForm
from django.contrib import messages
from django.db.models import Count
from athletes.models import Athlete
from coaches.models import Coach
from events.models import Event
from core.models import Sport, Campus, Team
from users.models import CustomUser
from .models import Statistic # Add this import
from .forms import StatisticForm

from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import SportForm, CampusForm 
import datetime
import csv
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

def dashboard(request):
    """
    Handles the main dashboard for both public visitors and authenticated users,
    providing either a general overview or a personalized view of their data.
    """
    # --- Data for EVERYONE ---
    # To get the sport and campus, we now go through the 'team' relationship.
    recent_athletes = Athlete.objects.select_related(
        'user', 'team', 'team__sport', 'team__campus'
    ).order_by('-user__date_joined')[:10]


    # --- Personalized Data (for logged-in users only) ---
    my_events = None
    my_athletes = None
    my_coach = None

    if request.user.is_authenticated:
        # For a logged-in COACH
        if request.user.role == CustomUser.Role.COACH:
            try:
                coach_profile = request.user.coach
                if coach_profile.team:
                    # Get events where participants are from the coach's team
                    my_events = Event.objects.filter(
                        participants__team=coach_profile.team
                    ).distinct().order_by('start_time')
                # Get all athletes assigned to this coach
                my_athletes = Athlete.objects.filter(coach=coach_profile).select_related('user')
            except Coach.DoesNotExist:
                pass

        # For a logged-in ATHLETE
        elif request.user.role == CustomUser.Role.ATHLETE:
            try:
                athlete_profile = request.user.athlete
                # Get all events the athlete is participating in
                my_events = athlete_profile.attended_events.all().order_by('start_time')
                # Get the athlete's assigned coach
                my_coach = athlete_profile.coach
            except Athlete.DoesNotExist:
                pass

    # --- Final Context for Template ---
    context = {
        'recent_athletes': recent_athletes,
        'my_events': my_events,
        'my_athletes': my_athletes,
        'my_coach': my_coach,
    }
    return render(request, 'core/dashboard.html', context)

@login_required
def feedback_view(request):
    # Prevent users from submitting feedback multiple times
    if Feedback.objects.filter(user=request.user).exists():
        messages.info(request, "You have already submitted your feedback. Thank you!")
        return redirect('dashboard')

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            messages.success(request, "Thank you! Your feedback has been submitted successfully.")
            return redirect('dashboard')
    else:
        form = FeedbackForm()

    return render(request, 'core/feedback.html', {'form': form})


class SportListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Sport
    template_name = 'core/sport_list.html'
    context_object_name = 'sports'

    def test_func(self): return self.request.user.role == CustomUser.Role.ADMINISTRATOR
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sport_form'] = SportForm()
        return context

class SportCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Sport
    form_class = SportForm
    success_url = reverse_lazy('sport-list')
    def test_func(self): return self.request.user.role == CustomUser.Role.ADMINISTRATOR


class CampusListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Campus
    template_name = 'core/campus_list.html'
    context_object_name = 'campuses'
    def test_func(self): return self.request.user.role == CustomUser.Role.ADMINISTRATOR
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campus_form'] = CampusForm()
        return context

class CampusCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Campus
    form_class = CampusForm
    success_url = reverse_lazy('campus-list')
    def test_func(self): return self.request.user.role == CustomUser.Role.ADMINISTRATOR


class SportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Sport
    form_class = SportForm
    template_name = 'core/sport_form.html' # A generic form template
    success_url = reverse_lazy('sport-list')
    def test_func(self): return self.request.user.role == CustomUser.Role.ADMINISTRATOR

class SportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Sport
    template_name = 'core/sport_confirm_delete.html' # The template that is missing
    success_url = reverse_lazy('sport-list')
    def test_func(self): return self.request.user.role == CustomUser.Role.ADMINISTRATOR

# --- Do the same for Campus ---
class CampusUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Campus
    form_class = CampusForm
    template_name = 'core/campus_form.html'
    success_url = reverse_lazy('campus-list')
    def test_func(self): return self.request.user.role == CustomUser.Role.ADMINISTRATOR

class CampusDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Campus
    template_name = 'core/campus_confirm_delete.html' # The missing template
    success_url = reverse_lazy('campus-list')
    def test_func(self): return self.request.user.role == CustomUser.Role.ADMINISTRATOR

    
@login_required
def live_search(request):
    """
    A view that handles live search queries from the navbar.
    Returns a JSON response with matching users (athletes and coaches).
    """
    # Get the search query from the GET parameters (e.g., /api/live-search/?q=john)
    query = request.GET.get('q', '')
    results = []

    # Only perform a search if the query is at least 2 characters long
    if len(query) >= 2:
        # Search for users who are either an Athlete or a Coach
        # and whose first name, last name, or username contains the query.
        # Q objects are used for complex OR queries.
        matching_users = CustomUser.objects.filter(
            Q(role__in=[CustomUser.Role.ATHLETE, CustomUser.Role.COACH]) &
            (Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(username__icontains=query))
        ).select_related('athlete', 'coach')[:10] # Limit to 10 results

        for user in matching_users:
            url = '#' # Default URL
            # Determine the correct profile URL based on the user's role
            if hasattr(user, 'athlete') and user.athlete:
                url = user.athlete.get_absolute_url()
            elif hasattr(user, 'coach') and user.coach:
                url = user.coach.get_absolute_url()
            
            results.append({
                'name': user.get_full_name(),
                'role': user.get_role_display(),
                'image_url': user.image.url if user.image else None,
                'url': url,
            })
    
    return JsonResponse({'results': results})


class SettingsDashboardView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Team
    template_name = 'core/settings_dashboard.html'
    context_object_name = 'teams'

    def test_func(self):
        # Only Administrators can access the settings page
        return self.request.user.role == CustomUser.Role.ADMINISTRATOR

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_form'] = TeamForm() # Add the form for creating a new team
        return context

class TeamCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy('settings-dashboard') # Redirect back to settings

    def form_valid(self, form):
        messages.success(self.request, f"Team '{form.instance}' created successfully.")
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.role == CustomUser.Role.ADMINISTRATOR
    

class SportStatisticsListView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Sport
    template_name = 'core/sport_statistics.html'
    context_object_name = 'sport'

    def test_func(self):
        return self.request.user.role == CustomUser.Role.ADMINISTRATOR

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the sport object from the view
        sport = self.get_object()
        # Get all statistics related to this sport
        context['statistics'] = Statistic.objects.filter(sport=sport)
        # Add an empty form for creating a new statistic
        context['statistic_form'] = StatisticForm(initial={'sport': sport})
        return context

class StatisticCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Statistic
    form_class = StatisticForm
    
    def test_func(self):
        return self.request.user.role == CustomUser.Role.ADMINISTRATOR

    def get_success_url(self):
        """
        Dynamically determines the redirect URL after a statistic is successfully created.
        """
        # 'self.object' is the new Statistic object that was just created.
        messages.success(self.request, f"Statistic '{self.object.name}' added successfully.")
        # We build the URL to go back to the list page for the sport this statistic belongs to.
        return reverse('sport-statistics', kwargs={'pk': self.object.sport.pk})