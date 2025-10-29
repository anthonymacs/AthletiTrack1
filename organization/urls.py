# organization/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('sport/<int:sport_id>/', views.sport_detail_view, name='sport-detail'),
    path('campus/<int:campus_id>/', views.campus_detail_view, name='campus-detail'),
    path('settings/', views.settings_dashboard_view, name='settings-dashboard'),

    path('teams/', views.TeamListView.as_view(), name='team-list'),
    path('teams/add/', views.TeamCreateView.as_view(), name='team-add'),
    path('teams/<int:pk>/edit/', views.TeamUpdateView.as_view(), name='team-edit'),
    path('teams/<int:pk>/delete/', views.TeamDeleteView.as_view(), name='team-delete'),
]