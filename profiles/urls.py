"""
URL configuration for the profiles application.

This module defines the URL patterns for the profiles application,
mapping URL paths to their corresponding view functions. The URLs
are namespaced under 'profiles' to avoid conflicts with other applications.

URL Patterns:
    '' (empty): Maps to profiles list view (profiles:index)
    '<str:username>/': Maps to profile detail view (profiles:profile)

The app_name provides namespace isolation for URL reverse lookups.
"""
from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
