"""
Tests for profiles views.

This module contains unit and integration tests for the profiles views,
using pytest.mark.django_db for database access.
"""
import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User

from profiles.models import Profile


class TestProfilesViews:
    """Test cases for profiles views."""

    @pytest.mark.django_db
    def test_profiles_index_view(self):
        """Test the profiles index view displays all profiles."""
        client = Client()

        # Create test data
        user1 = User.objects.create_user(
            username='user1',
            email='user1@example.com',
            first_name='User',
            last_name='One'
        )

        user2 = User.objects.create_user(
            username='user2',
            email='user2@example.com',
            first_name='User',
            last_name='Two'
        )

        profile1 = Profile.objects.create(
            user=user1,
            favorite_city='Paris'
        )

        profile2 = Profile.objects.create(
            user=user2,
            favorite_city='London'
        )

        # Test the view
        url = reverse('profiles:index')
        response = client.get(url)

        assert response.status_code == 200
        assert 'profiles_list' in response.context
        assert len(response.context['profiles_list']) == 2
        assert profile1 in response.context['profiles_list']
        assert profile2 in response.context['profiles_list']
        assert 'user1' in response.content.decode()
        assert 'user2' in response.content.decode()

    @pytest.mark.django_db
    def test_profile_detail_view(self):
        """Test the profile detail view displays specific profile info."""
        client = Client()

        # Create test data
        user = User.objects.create_user(
            username='detailuser',
            email='detail@example.com',
            first_name='Detail',
            last_name='User'
        )

        profile = Profile.objects.create(
            user=user,
            favorite_city='Tokyo'
        )

        # Test the view
        url = reverse('profiles:profile', kwargs={'username': user.username})
        response = client.get(url)

        assert response.status_code == 200
        assert response.context['profile'] == profile
        assert 'detailuser' in response.content.decode()
        assert 'Detail' in response.content.decode()
        assert 'User' in response.content.decode()
        assert 'Tokyo' in response.content.decode()

    @pytest.mark.django_db
    def test_profile_detail_view_not_found(self):
        """Test the profile detail view returns 404 for non-existent profile."""
        client = Client()

        url = reverse('profiles:profile', kwargs={'username': 'nonexistent'})
        response = client.get(url)

        assert response.status_code == 404

    @pytest.mark.django_db
    def test_empty_profiles_index(self):
        """Test the profiles index view when no profiles exist."""
        client = Client()

        url = reverse('profiles:index')
        response = client.get(url)

        assert response.status_code == 200
        assert 'profiles_list' in response.context
        assert len(response.context['profiles_list']) == 0

    @pytest.mark.django_db
    def test_profile_detail_user_without_profile(self):
        """Test profile detail view for user without profile returns 404."""
        client = Client()

        # Create user without profile
        User.objects.create_user(
            username='noprofileuser',
            email='noprofile@example.com'
        )

        url = reverse('profiles:profile', kwargs={'username': 'noprofileuser'})
        response = client.get(url)

        assert response.status_code == 404

    @pytest.mark.django_db
    def test_profiles_index_template_used(self):
        """Test that the correct template is used for profiles index."""
        client = Client()

        url = reverse('profiles:index')
        response = client.get(url)

        assert response.status_code == 200
        assert 'profiles/index.html' in [t.name for t in response.templates]

    @pytest.mark.django_db
    def test_profile_detail_template_used(self):
        """Test that the correct template is used for profile detail."""
        client = Client()

        user = User.objects.create_user(
            username='templateuser',
            email='template@example.com'
        )

        Profile.objects.create(
            user=user,
            favorite_city='Madrid'
        )

        url = reverse('profiles:profile', kwargs={'username': user.username})
        response = client.get(url)

        assert response.status_code == 200
        assert 'profiles/profile.html' in [t.name for t in response.templates]

    @pytest.mark.django_db
    def test_profile_with_empty_favorite_city(self):
        """Test profile detail view with empty favorite city."""
        client = Client()

        user = User.objects.create_user(
            username='emptycityuser',
            email='emptycity@example.com',
            first_name='Empty',
            last_name='City'
        )

        profile = Profile.objects.create(
            user=user,
            favorite_city=''
        )

        url = reverse('profiles:profile', kwargs={'username': user.username})
        response = client.get(url)

        assert response.status_code == 200
        assert response.context['profile'] == profile
        assert 'emptycityuser' in response.content.decode()
