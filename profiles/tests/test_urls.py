"""
Tests for profiles URL configuration.

This module contains tests for the profiles URL patterns and routing,
using pytest.mark.django_db for database access when needed.
"""
import pytest
from django.urls import reverse, resolve

from profiles.views import index, profile


class TestProfilesUrls:
    """Test cases for profiles URL configuration."""

    def test_profiles_index_url_resolves(self):
        """Test that the profiles index URL resolves correctly."""
        url = reverse('profiles:index')
        assert url == '/profiles/'

        resolver = resolve('/profiles/')
        assert resolver.func == index
        assert resolver.namespace == 'profiles'
        assert resolver.url_name == 'index'

    def test_profile_detail_url_resolves(self):
        """Test that the profile detail URL resolves correctly."""
        username = 'testuser'
        url = reverse('profiles:profile', kwargs={'username': username})
        assert url == f'/profiles/{username}/'

        resolver = resolve(f'/profiles/{username}/')
        assert resolver.func == profile
        assert resolver.namespace == 'profiles'
        assert resolver.url_name == 'profile'
        assert resolver.kwargs == {'username': username}

    @pytest.mark.django_db
    def test_profiles_index_url_name(self):
        """Test that the profiles index URL name works correctly."""
        url = reverse('profiles:index')
        assert url == '/profiles/'

    @pytest.mark.django_db
    def test_profile_detail_url_name_with_username(self):
        """Test profile detail URL name with various usernames."""
        # Test with regular username
        url = reverse('profiles:profile', kwargs={'username': 'regularuser'})
        assert url == '/profiles/regularuser/'

        # Test with username containing numbers
        url = reverse('profiles:profile', kwargs={'username': 'user123'})
        assert url == '/profiles/user123/'

        # Test with username containing underscores
        url = reverse('profiles:profile', kwargs={'username': 'user_name'})
        assert url == '/profiles/user_name/'

    def test_profile_url_pattern_validation(self):
        """Test that profile URL pattern validates correctly."""
        # Test valid patterns
        valid_usernames = ['user', 'user123', 'user_name', 'User', 'USER']

        for username in valid_usernames:
            url = f'/profiles/{username}/'
            resolver = resolve(url)
            assert resolver.func == profile
            assert resolver.kwargs['username'] == username

    def test_profiles_namespace(self):
        """Test that profiles URLs use the correct namespace."""
        index_url = reverse('profiles:index')
        profile_url = reverse('profiles:profile', kwargs={'username': 'test'})

        assert index_url.startswith('/profiles/')
        assert profile_url.startswith('/profiles/')

        # Verify namespace resolution
        index_resolver = resolve(index_url)
        profile_resolver = resolve(profile_url)

        assert index_resolver.namespace == 'profiles'
        assert profile_resolver.namespace == 'profiles'

    def test_url_patterns_count(self):
        """Test that we have the expected number of URL patterns."""
        from profiles.urls import urlpatterns
        assert len(urlpatterns) == 2

    def test_url_pattern_names(self):
        """Test that URL patterns have the correct names."""
        from profiles.urls import urlpatterns

        url_names = [pattern.name for pattern in urlpatterns]
        expected_names = ['index', 'profile']

        assert set(url_names) == set(expected_names)
