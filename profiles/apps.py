"""
Application configuration for the profiles application.

This module contains the Django application configuration for the profiles
app, which handles user profile management and extended user information.
"""
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration class for the profiles application.

    This class defines the configuration settings for the profiles Django
    application, including the default auto field type and application name.

    Attributes:
        default_auto_field (str): Specifies the default primary key field type
                                 for models that don't define a primary key.
        name (str): The full Python path to the application module.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
