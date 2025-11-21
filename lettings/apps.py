"""
Application configuration for the lettings application.

This module contains the Django application configuration for the lettings
app, which handles property rental listings and address management.
"""
from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    Configuration class for the lettings application.

    This class defines the configuration settings for the lettings Django
    application, including the default auto field type and application name.

    Attributes:
        default_auto_field (str): Specifies the default primary key field type
                                 for models that don't define a primary key.
        name (str): The full Python path to the application module.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lettings'
