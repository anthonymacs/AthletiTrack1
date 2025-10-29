# reports/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_dashboard, name='report-dashboard'),
    path('chart/performance-trend/', views.performance_trend_chart, name='performance-trend-chart'),
    path('export/athletes-csv/', views.export_athletes_csv, name='export-athletes-csv'),

    path('', views.report_dashboard, name='report-dashboard'),
    # New API endpoint for chart data
    path('api/performance-data/', views.get_performance_chart_data, name='get-performance-chart-data'),

    #path('api/stats-pie-data/', views.get_stats_pie_chart_data, name='get-stats-pie-data'),
    path('api/stats-summary-data/', views.get_stats_summary_data, name='get-stats-summary-data'), # <-- NEW

    path('api/calendar-events/', views.get_calendar_events, name='calendar-events'),
    path('api/stats-for-team/', views.get_stats_for_team, name='stats-for-team'),
]