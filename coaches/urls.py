# coaches/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CoachListView.as_view(), name='coach-list'),
    path('add/', views.CoachCreateView.as_view(), name='coach-add'),
    path('<int:pk>/edit/', views.CoachUpdateView.as_view(), name='coach-edit'),
    path('<int:pk>/delete/', views.CoachDeleteView.as_view(), name='coach-delete'),
    path('<int:pk>/', views.CoachDetailView.as_view(), name='coach-detail'), # Add this line
]