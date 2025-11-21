"""
Django admin configuration for the lettings application.

This module registers models with the Django admin interface to provide
a web-based administrative interface for managing addresses and lettings.
The admin interface allows authorized users to create, read, update, and
delete address and letting records through a user-friendly web interface.

Registered Models:
    Address: For managing property addresses
    Letting: For managing rental property listings
"""
from django.contrib import admin

from .models import Address, Letting

# Register models with Django admin
admin.site.register(Address)
admin.site.register(Letting)
