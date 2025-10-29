# organization/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from core.forms import TeamForm
from core.models import Sport, Team, Campus

@login_required
def sport_detail_view(request, sport_id):
    sport = get_object_or_404(Sport, pk=sport_id)
    
    # Get all teams related to this sport, and pre-fetch their athletes
    teams_in_sport = Team.objects.filter(sport=sport).prefetch_related('athlete_set__user').order_by('campus__name', 'gender')

    context = {
        'sport': sport,
        'teams_in_sport': teams_in_sport,
    }
    return render(request, 'organization/sport_detail.html', context)


@login_required
def campus_detail_view(request, campus_id):
    campus = get_object_or_404(Campus, pk=campus_id)
    
    # Get all teams at this campus
    teams_at_campus = Team.objects.filter(campus=campus).prefetch_related('athlete_set__user').order_by('sport__name', 'gender')

    context = {
        'campus': campus,
        'teams_at_campus': teams_at_campus,
    }
    return render(request, 'organization/campus_detail.html', context)


@login_required
def settings_dashboard_view(request):
    # Add a permission check later if needed
    return render(request, 'organization/settings_dashboard.html')

class TeamListView(LoginRequiredMixin, ListView):
    model = Team
    template_name = 'organization/team_list.html'
    context_object_name = 'teams'

class TeamCreateView(LoginRequiredMixin, CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'organization/team_form.html'
    success_url = reverse_lazy('team-list')

class TeamUpdateView(LoginRequiredMixin, UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'organization/team_form.html'
    success_url = reverse_lazy('team-list')

class TeamDeleteView(LoginRequiredMixin, DeleteView):
    model = Team
    template_name = 'organization/team_confirm_delete.html'
    success_url = reverse_lazy('team-list')