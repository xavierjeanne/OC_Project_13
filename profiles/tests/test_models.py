"""
Tests for profiles models.

This module contains unit tests for the Profile model,
using pytest.mark.django_db for database access.
"""
import pytest
from django.contrib.auth.models import User
from django.db import IntegrityError

from profiles.models import Profile


class TestProfile:
    """Test cases for the Profile model."""

    @pytest.mark.django_db
    def test_profile_creation(self):
        """Test that a profile can be created with valid data."""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        profile = Profile.objects.create(
            user=user,
            favorite_city='Paris'
        )
        
        assert profile.user == user
        assert profile.favorite_city == 'Paris'

    @pytest.mark.django_db
    def test_profile_str_method(self):
        """Test the string representation of a profile."""
        user = User.objects.create_user(
            username='profileuser',
            email='profile@example.com'
        )
        
        profile = Profile.objects.create(
            user=user,
            favorite_city='London'
        )
        
        assert str(profile) == 'profileuser'

    @pytest.mark.django_db
    def test_profile_favorite_city_blank(self):
        """Test that favorite_city can be blank."""
        user = User.objects.create_user(
            username='blankuser',
            email='blank@example.com'
        )
        
        profile = Profile.objects.create(
            user=user,
            favorite_city=''
        )
        
        assert profile.favorite_city == ''
        assert profile.user == user

    @pytest.mark.django_db
    def test_profile_cascade_delete(self):
        """Test that deleting a user also deletes the associated profile."""
        user = User.objects.create_user(
            username='deleteuser',
            email='delete@example.com'
        )
        
        profile = Profile.objects.create(
            user=user,
            favorite_city='Berlin'
        )
        
        profile_id = profile.id
        
        # Delete the user
        user.delete()
        
        # Verify the profile was also deleted
        assert not Profile.objects.filter(id=profile_id).exists()

    @pytest.mark.django_db
    def test_profile_one_to_one_relationship(self):
        """Test the one-to-one relationship between user and profile."""
        user = User.objects.create_user(
            username='uniqueuser',
            email='unique@example.com'
        )
        
        profile = Profile.objects.create(
            user=user,
            favorite_city='Tokyo'
        )
        
        # Test the relationship works both ways
        assert profile.user == user
        assert user.profile == profile

    @pytest.mark.django_db
    def test_profile_unique_user_constraint(self):
        """Test that a user can only have one profile."""
        user = User.objects.create_user(
            username='constraintuser',
            email='constraint@example.com'
        )
        
        # Create first profile
        Profile.objects.create(
            user=user,
            favorite_city='Madrid'
        )
        
        # Try to create second profile for the same user
        with pytest.raises(IntegrityError):
            Profile.objects.create(
                user=user,
                favorite_city='Barcelona'
            )

    @pytest.mark.django_db
    def test_profile_verbose_name_plural(self):
        """Test that the plural name is correctly set."""
        assert Profile._meta.verbose_name_plural == 'profiles'

    @pytest.mark.django_db
    def test_profile_favorite_city_max_length(self):
        """Test that favorite_city respects max_length constraint."""
        user = User.objects.create_user(
            username='longcityuser',
            email='longcity@example.com'
        )
        
        # Create profile with long city name (should work up to 64 chars)
        long_city = 'A' * 64
        profile = Profile.objects.create(
            user=user,
            favorite_city=long_city
        )
        
        assert profile.favorite_city == long_city
        assert len(profile.favorite_city) == 64
