# reports/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from athletes.models import Athlete, PerformanceStat
from events.models import Event
from core.models import Sport, Campus, Team, Statistic
from users.models import CustomUser
from django.urls import reverse
from django.db import models
import datetime
from coaches.models import Coach
from django.http import JsonResponse, HttpResponse
from django.db.models import Count, Avg, Max, Min, Sum, Q, F
from django.db.models.functions import Cast
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
import csv
import re
from django.utils import timezone


@login_required
def report_dashboard(request):
    """
    Displays a comprehensive analytics dashboard, with data scoped to the
    user's role (Admin sees all, Coach sees their team's data).
    """
    user = request.user
    if not user.role in [CustomUser.Role.COACH, CustomUser.Role.ADMINISTRATOR]:
        messages.error(request, "You are not authorized to view this page.")
        return redirect('dashboard')

    # --- DEFINE THE BASE QUERYSETS BASED ON USER ROLE ---
    athlete_queryset = Athlete.objects.all()
    coach_queryset = Coach.objects.all()
    team_queryset = Team.objects.all()
    campus_queryset = Campus.objects.all()
    event_queryset = Event.objects.all()
    report_title = "University-Wide Analytics"

    if user.role == CustomUser.Role.COACH and hasattr(user, 'coach') and user.coach.team:
        coachs_team = user.coach.team
        athlete_queryset = Athlete.objects.filter(team=coachs_team)
        coach_queryset = Coach.objects.filter(team=coachs_team)
        team_queryset = Team.objects.filter(pk=coachs_team.pk)
        campus_queryset = Campus.objects.filter(pk=coachs_team.campus.pk)
        event_queryset = Event.objects.filter(participants__team=coachs_team).distinct()
        report_title = f"Analytics for Team: {coachs_team}"
    
    # --- NOW, ALL QUERIES USE THE PRE-FILTERED QUERYSETS ---
    
    # --- OVERVIEW STATISTICS ---
    overview_stats = {
        'total_athletes': athlete_queryset.count(),
        'total_male_athletes': athlete_queryset.filter(user__gender=CustomUser.Gender.MALE).count(),
        'total_female_athletes': athlete_queryset.filter(user__gender=CustomUser.Gender.FEMALE).count(),
        'athletes_by_campus': campus_queryset.annotate(count=Count('team__athlete', distinct=True)).order_by('-count'),
        'total_coaches': coach_queryset.count(),
        'total_male_coaches': coach_queryset.filter(user__gender=CustomUser.Gender.MALE).count(),
        'total_female_coaches': coach_queryset.filter(user__gender=CustomUser.Gender.FEMALE).count(),
        'coaches_by_campus': campus_queryset.annotate(count=Count('team__coach', distinct=True)).order_by('-count'),
    }

    # --- ATHLETE DISTRIBUTION BY SPORT & GENDER (Admin Only) ---
    athletes_by_sport_gender = None
    if user.role == CustomUser.Role.ADMINISTRATOR:
        athletes_by_sport_gender = Sport.objects.annotate(
            total_athletes=Count('team__athlete', distinct=True),
            male_athletes=Count('team__athlete', filter=Q(team__athlete__user__gender=CustomUser.Gender.MALE), distinct=True),
            female_athletes=Count('team__athlete', filter=Q(team__athlete__user__gender=CustomUser.Gender.FEMALE), distinct=True)
        ).order_by('-total_athletes')

    # --- GAME HISTORY (scoped) ---
    game_history = event_queryset.filter(
        end_time__lt=timezone.now(),
        our_score__isnull=False
    ).select_related('coach_in_charge__user').order_by('-end_time')[:5]

    # --- TEAM-BASED KPI CALCULATIONS (scoped) ---
    completed_events_qs = event_queryset.filter(
        end_time__lt=timezone.now(),
        our_score__isnull=False,
        opponent_score__isnull=False
    )
    total_wins = completed_events_qs.filter(our_score__gt=F('opponent_score')).count()
    total_losses = completed_events_qs.filter(our_score__lt=F('opponent_score')).count()
    total_games = total_wins + total_losses
    winrate = (total_wins / total_games * 100) if total_games > 0 else 0

    kpis = {
        'total_wins': total_wins,
        'total_losses': total_losses,
        'winrate': f"{winrate:.1f}%",
    }

    # --- DATA FOR DYNAMIC CHARTS (scoped) ---
    performance_stats_qs = PerformanceStat.objects.filter(athlete__in=athlete_queryset)
    unique_stat_names = performance_stats_qs.values_list('statistic__name', flat=True).distinct().order_by('statistic__name')

    context = {
        'report_title': report_title,
        'overview_stats': overview_stats,
        'athletes_by_sport_gender': athletes_by_sport_gender,
        'game_history': game_history,
        'kpis': kpis,
        'all_teams': team_queryset.order_by('sport__name'),
        'unique_stat_names': unique_stat_names,
    }
    return render(request, 'reports/dashboard.html', context)

@login_required
def get_performance_chart_data(request):
    """
    A single API view to provide JSON data for all performance charts.
    Handles team comparisons and individual multi-line trends.
    """
    team_id = request.GET.get('team_id')
    athlete_id = request.GET.get('athlete_id')
    stat_name = request.GET.get('stat_name')
    chart_type = request.GET.get('chart_type')

    # --- Mode 1: Multi-line Trend for a single athlete (athlete_detail page) ---
    if chart_type == 'multiline_trend' and athlete_id:
        # Query all stats for the athlete, ordered by the event's date
        stats = PerformanceStat.objects.filter(
            athlete_id=athlete_id
        ).select_related('statistic', 'event').order_by('event__start_time')
        
        datasets = {}
        # Get a unique, sorted list of all event datetimes
        all_events = sorted(list(stats.values_list('event__start_time', flat=True).distinct()))
        # Format those datetimes into clean labels for the chart's X-axis
        labels = [dt.strftime('%b %d, %Y') for dt in all_events]

        for stat in stats:
            # Skip any legacy stats that might not be linked to an event
            if not stat.event:
                continue

            stat_label = stat.statistic.name
            if stat_label not in datasets:
                datasets[stat_label] = {
                    'label': stat_label,
                    'data': [None] * len(all_events), # Create a placeholder for each event
                    'tension': 0.1,
                    'fill': False,
                }
            
            # Find the correct position for this data point in the list
            event_index = all_events.index(stat.event.start_time)
            try:
                numeric_part = re.search(r'\d+\.?\d*', str(stat.value))
                if numeric_part:
                    datasets[stat_label]['data'][event_index] = float(numeric_part.group())
            except (ValueError, TypeError):
                pass # Leave as None if value is not numeric

        return JsonResponse({'labels': labels, 'datasets': list(datasets.values())})

    # --- Mode 2: Team Comparison Chart (reports page) ---
    elif chart_type == 'comparison' and team_id and stat_name:
        stats = PerformanceStat.objects.filter(
            athlete__team_id=team_id,
            statistic__name=stat_name
        ).select_related('athlete__user')

        athlete_data = {}
        for stat in stats:
            athlete_name = stat.athlete.user.get_full_name()
            try:
                numeric_part = re.search(r'\d+\.?\d*', str(stat.value))
                if numeric_part:
                    value = float(numeric_part.group())
                    if athlete_name not in athlete_data or value < athlete_data[athlete_name]:
                        athlete_data[athlete_name] = value
            except (ValueError, TypeError):
                continue
        
        sorted_athletes = sorted(athlete_data.items(), key=lambda item: item[1])
        labels = [name for name, perf in sorted_athletes]
        data = [perf for name, perf in sorted_athletes]
        return JsonResponse({'labels': labels, 'data': data})
    
    # If no valid combination of parameters is provided, return an error.
    return JsonResponse({'error': 'Invalid or missing parameters'}, status=400)

@login_required
def export_athletes_csv(request):
    """
    Generates a CSV file of all athletes with their team information.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="athletitrack_athletes_{datetime.date.today()}.csv"'

    writer = csv.writer(response)
    # Write the header row
    writer.writerow(['User ID', 'First Name', 'Last Name', 'Email', 'Gender', 'Birthday', 'Team', 'Coach'])

    # Get all athletes and pre-fetch related data for efficiency
    athletes = Athlete.objects.all().select_related('user', 'team', 'team__sport', 'team__campus', 'coach__user')

    for athlete in athletes:
        writer.writerow([
            athlete.user.id,
            athlete.user.first_name,
            athlete.user.last_name,
            athlete.user.email,
            athlete.user.get_gender_display(),
            athlete.birthday,
            str(athlete.team) if athlete.team else 'N/A', # Use the __str__ method of the Team model
            athlete.coach.user.get_full_name() if athlete.coach else 'N/A'
        ])

    return response

@login_required
def performance_trend_chart(request):
    """
    Provides data for the performance trend chart.
    This view is intended to be called via a Fetch/AJAX request.
    """
    athlete_id = request.GET.get('athlete_id')
    stat_name = request.GET.get('stat_name')

    # Query for the stats based on the GET parameters
    stats = PerformanceStat.objects.filter(
        athlete_id=athlete_id,
        statistic_name=stat_name
    ).order_by('year')

    # Prepare the data in a chart-friendly format
    labels = [stat.year for stat in stats]
    data = [float(stat.value.rstrip('sm')) for stat in stats] # Basic cleaning of data for plotting

    chart_data = {
        'labels': labels,
        'data': data,
    }
    return JsonResponse(chart_data)


def export_athletes_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="evsu_athletes_{datetime.date.today()}.csv"'

    writer = csv.writer(response)
    # Write the header row
    writer.writerow(['ID', 'First Name', 'Last Name', 'Email', 'Sport', 'Campus'])

    # Write data rows
    athletes = Athlete.objects.all().select_related('user', 'sport', 'campus')
    for athlete in athletes:
        writer.writerow([
            athlete.user.id,
            athlete.user.first_name,
            athlete.user.last_name,
            athlete.user.email,
            athlete.sport.name if athlete.sport else 'N/A',
            athlete.campus.name if athlete.campus else 'N/A'
        ])

    return response

@login_required
def get_stats_summary_data(request):
    """
    Provides aggregated data for an athlete's or team's statistics.
    It sums the 'value' of each statistic type.
    """
    team_id = request.GET.get('team_id')
    athlete_id = request.GET.get('athlete_id')

    queryset = PerformanceStat.objects.all()

    if team_id:
        queryset = queryset.filter(athlete__team_id=team_id)
    elif athlete_id:
        queryset = queryset.filter(athlete_id=athlete_id)
    
    # --- THIS IS THE KEY CHANGE ---
    # 1. Cast the 'value' field (which is text) to a numeric type (Decimal).
    # 2. Group by the statistic's name.
    # 3. For each group, calculate the SUM of the now-numeric values.
    stats_summary = queryset.annotate(
        numeric_value=Cast('value', models.DecimalField(max_digits=10, decimal_places=2))
    ).values(
        'statistic__name'
    ).annotate(
        total_value=Sum('numeric_value')
    ).order_by('-total_value')
    # --- END OF CHANGE ---

    # The keys in the resulting dictionary will now be 'statistic__name' and 'total_value'
    labels = [item['statistic__name'] for item in stats_summary]
    data = [item['total_value'] for item in stats_summary]

    return JsonResponse({'labels': labels, 'data': data})


@login_required
def get_calendar_events(request):
    """
    An API-like view that provides event data in the format
    that the FullCalendar library expects.
    """
    # Filter events based on the user's role, just like the event list page
    user = request.user
    queryset = Event.objects.none()

    if user.role == CustomUser.Role.ADMINISTRATOR:
        queryset = Event.objects.all()
    elif user.role == CustomUser.Role.COACH and hasattr(user, 'coach') and user.coach.team:
        queryset = Event.objects.filter(participants__team=user.coach.team).distinct()
    elif user.role == CustomUser.Role.ATHLETE and hasattr(user, 'athlete'):
        queryset = user.athlete.attended_events.all()

    # Format the event data into a list of dictionaries
    events_data = []
    for event in queryset:
        events_data.append({
            'title': event.name,
            'start': event.start_time,
            'end': event.end_time,
            'url': reverse('event-detail', kwargs={'pk': event.pk}), # Make the event clickable
            'color': '#0d6efd' if 'practice' in event.name.lower() else '#198754', # Example custom color
        })
    
    return JsonResponse(events_data, safe=False)

@login_required
def get_stats_for_team(request):
    """
    An API-like view that, given a team_id, returns a JSON list of
    the statistics associated with that team's sport.
    """
    team_id = request.GET.get('team_id')
    if not team_id:
        return JsonResponse({'error': 'Missing team_id parameter'}, status=400)
    
    try:
        # Find the team and then get all statistics for that team's sport
        team = Team.objects.get(pk=team_id)
        stats = Statistic.objects.filter(sport=team.sport).values('name')
        return JsonResponse(list(stats), safe=False)
    except Team.DoesNotExist:
        return JsonResponse({'error': 'Team not found'}, status=404)