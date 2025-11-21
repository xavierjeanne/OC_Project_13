"""
URL configuration for the lettings application.

This module defines the URL patterns for the lettings application,
mapping URL paths to their corresponding view functions. The URLs
are namespaced under 'lettings' to avoid conflicts with other applications.

URL Patterns:
    '' (empty): Maps to lettings list view (lettings:index)
    '<int:letting_id>/': Maps to letting detail view (lettings:letting)

The app_name provides namespace isolation for URL reverse lookups.
"""
from django.urls import path
from . import views

app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
