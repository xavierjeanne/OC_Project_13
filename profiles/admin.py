"""
Django admin configuration for the profiles application.

This module registers the Profile model with the Django admin interface
to provide a web-based administrative interface for managing user profiles.
The admin interface allows authorized users to view and manage user profile
information including favorite cities and associated user accounts.

Registered Models:
    Profile: For managing user profile information and favorite cities
"""
from django.contrib import admin

from .models import Profile

# Register Profile model with Django admin
admin.site.register(Profile)
