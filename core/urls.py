# core/urls.py
from django.urls import path
from . import views
from .views import SettingsDashboardView, TeamCreateView
from .views import SportListView, SportCreateView, SportUpdateView, SportDeleteView
from .views import CampusListView, CampusCreateView, CampusUpdateView, CampusDeleteView

urlpatterns = [
    # You may want to create a urls.py for core if you haven't already
    # and include it in the main urls.py
    path('feedback/', views.feedback_view, name='feedback'),
    #Spath('export/athletes-csv/', views.export_athletes_csv, name='export-athletes-csv'),

    path('sports/', views.SportListView.as_view(), name='sport-list'),
    path('sports/add/', views.SportCreateView.as_view(), name='sport-add'), 

    path('campuses/', views.CampusListView.as_view(), name='campus-list'),
    path('campuses/add/', views.CampusCreateView.as_view(), name='campus-add'),

    path('sports/<int:pk>/edit/', views.SportUpdateView.as_view(), name='sport-edit'),
    path('sports/<int:pk>/delete/', views.SportDeleteView.as_view(), name='sport-delete'),
    path('campuses/<int:pk>/edit/', views.CampusUpdateView.as_view(), name='campus-edit'),
    path('campuses/<int:pk>/delete/', views.CampusDeleteView.as_view(), name='campus-delete'),

    path('api/live-search/', views.live_search, name='live-search'),

    path('settings/', SettingsDashboardView.as_view(), name='settings-dashboard'),
    path('settings/team/add/', TeamCreateView.as_view(), name='team-add'),

    path('settings/sport/<int:pk>/statistics/', views.SportStatisticsListView.as_view(), name='sport-statistics'),
    path('settings/statistic/add/', views.StatisticCreateView.as_view(), name='statistic-add'),

    path('settings/sports/', SportListView.as_view(), name='sport-list'),
    path('settings/sports/add/', SportCreateView.as_view(), name='sport-add'),
    path('settings/sports/<int:pk>/edit/', SportUpdateView.as_view(), name='sport-edit'),
    path('settings/sports/<int:pk>/delete/', SportDeleteView.as_view(), name='sport-delete'),

    path('settings/campuses/', CampusListView.as_view(), name='campus-list'),
    path('settings/campuses/add/', CampusCreateView.as_view(), name='campus-add'),
    path('settings/campuses/<int:pk>/edit/', CampusUpdateView.as_view(), name='campus-edit'),
    path('settings/campuses/<int:pk>/delete/', CampusDeleteView.as_view(), name='campus-delete'),
]

