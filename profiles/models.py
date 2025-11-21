"""
Models for the profiles application.

This module defines the user profile model that extends Django's built-in
User model with additional profile information. It provides a one-to-one
relationship to store extra user data not included in the default User model.

Models:
    Profile: Extended user profile with additional personal information
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model representing a user profile with extended information.

    This model extends Django's built-in User model by providing additional
    profile information through a one-to-one relationship. Each User can have
    exactly one Profile, and each Profile belongs to exactly one User.

    Attributes:
        user (OneToOneField): Reference to the associated Django User object.
                            When the User is deleted, the Profile is also deleted.
        favorite_city (CharField): User's favorite city (max 64 characters).
                                  This field is optional and can be blank.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        """Meta configuration for Profile model."""
        verbose_name_plural = "profiles"

    def __str__(self):
        """
        Return string representation of the profile.

        Returns:
            str: The username of the associated User object.
        """
        return self.user.username
