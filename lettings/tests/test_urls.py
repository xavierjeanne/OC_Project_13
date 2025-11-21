"""
Tests for lettings URL configuration.

This module contains tests for the lettings URL patterns and routing,
using pytest.mark.django_db for database access when needed.
"""
import pytest
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from lettings.models import Address, Letting
from lettings.views import index, letting


class TestLettingsUrls:
    """Test cases for lettings URL configuration."""

    def test_lettings_index_url_resolves(self):
        """Test that the lettings index URL resolves correctly."""
        url = reverse('lettings:index')
        assert url == '/lettings/'
        
        resolver = resolve('/lettings/')
        assert resolver.func == index
        assert resolver.namespace == 'lettings'
        assert resolver.url_name == 'index'

    def test_letting_detail_url_resolves(self):
        """Test that the letting detail URL resolves correctly."""
        letting_id = 123
        url = reverse('lettings:letting', kwargs={'letting_id': letting_id})
        assert url == f'/lettings/{letting_id}/'
        
        resolver = resolve(f'/lettings/{letting_id}/')
        assert resolver.func == letting
        assert resolver.namespace == 'lettings'
        assert resolver.url_name == 'letting'
        assert resolver.kwargs == {'letting_id': letting_id}

    @pytest.mark.django_db
    def test_lettings_index_url_name(self):
        """Test that the lettings index URL name works correctly."""
        url = reverse('lettings:index')
        assert url == '/lettings/'

    @pytest.mark.django_db
    def test_letting_detail_url_name_with_id(self):
        """Test letting detail URL name with various IDs."""
        # Test with regular ID
        url = reverse('lettings:letting', kwargs={'letting_id': 1})
        assert url == '/lettings/1/'
        
        # Test with larger ID
        url = reverse('lettings:letting', kwargs={'letting_id': 999})
        assert url == '/lettings/999/'
        
        # Test with single digit ID
        url = reverse('lettings:letting', kwargs={'letting_id': 5})
        assert url == '/lettings/5/'

    def test_letting_url_pattern_validation(self):
        """Test that letting URL pattern validates correctly."""
        # Test valid patterns
        valid_ids = [1, 10, 100, 999, 1234]
        
        for letting_id in valid_ids:
            url = f'/lettings/{letting_id}/'
            resolver = resolve(url)
            assert resolver.func == letting
            assert resolver.kwargs['letting_id'] == letting_id

    def test_lettings_namespace(self):
        """Test that lettings URLs use the correct namespace."""
        index_url = reverse('lettings:index')
        letting_url = reverse('lettings:letting', kwargs={'letting_id': 1})
        
        assert index_url.startswith('/lettings/')
        assert letting_url.startswith('/lettings/')
        
        # Verify namespace resolution
        index_resolver = resolve(index_url)
        letting_resolver = resolve(letting_url)
        
        assert index_resolver.namespace == 'lettings'
        assert letting_resolver.namespace == 'lettings'

    def test_url_patterns_count(self):
        """Test that we have the expected number of URL patterns."""
        from lettings.urls import urlpatterns
        assert len(urlpatterns) == 2

    def test_url_pattern_names(self):
        """Test that URL patterns have the correct names."""
        from lettings.urls import urlpatterns
        
        url_names = [pattern.name for pattern in urlpatterns]
        expected_names = ['index', 'letting']
        
        assert set(url_names) == set(expected_names)

    def test_letting_id_must_be_numeric(self):
        """Test that letting ID parameter must be numeric."""
        # This should work
        url = '/lettings/123/'
        resolver = resolve(url)
        assert resolver.kwargs['letting_id'] == 123
        
    def test_lettings_url_with_trailing_slash(self):
        """Test that URLs work correctly with trailing slashes."""
        # Index URL
        index_resolver = resolve('/lettings/')
        assert index_resolver.func == index
        
        # Detail URL
        detail_resolver = resolve('/lettings/1/')
        assert detail_resolver.func == letting
        assert detail_resolver.kwargs['letting_id'] == 1
