# athletes/urls.py
from django.urls import path
from . import views  # Use a single, simple import for views

urlpatterns = [
    # --- Core Roster and Detail Views ---
    path('', views.athlete_list, name='athlete-list'),
    path('<int:pk>/', views.athlete_detail, name='athlete-detail'),

    # --- Athlete Creation and Management ---
    # This path now correctly points to your new function-based view for adding a single athlete.
    #path('add/', views.athlete_create_view, name='athlete-add'),

    # The Update and Delete views are still classes, so they use .as_view()
    path('<int:pk>/edit/', views.AthleteUpdateView.as_view(), name='athlete-edit'),
    path('<int:pk>/delete/', views.AthleteDeleteView.as_view(), name='athlete-delete'),

    path('<int:pk>/stats/', views.manage_athlete_stats, name='manage-athlete-stats'),
    
   #path('add-bulk/', views.athlete_bulk_create_view, name='athlete-bulk-add'), # <-- ADD THIS
   path('add-bulk/', views.bulk_add_by_team_view, name='athlete-bulk-filtered'),
   
]