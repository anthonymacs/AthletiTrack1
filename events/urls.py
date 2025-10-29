# events/urls.py
from django.urls import path
from . import views  # Use a single, simple import for views

urlpatterns = [
    # --- Core Views ---
    path('', views.event_list, name='event-list'),
    path('<int:pk>/', views.event_detail, name='event-detail'),

    # --- Event Creation and Management ---
    # The primary way to create multiple events for a filtered group
    path('schedule/', views.schedule_events_view, name='event-schedule'),

    # --- Editing and Deleting ---
    path('<int:pk>/edit/', views.EventUpdateView.as_view(), name='event-edit'),
    path('<int:pk>/delete/', views.EventDeleteView.as_view(), name='event-delete'),
    path('<int:pk>/report/', views.game_report_view, name='game-report'),
]