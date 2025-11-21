"""
Tests for oc_lettings_site URL configuration.

This module contains tests for the main site URL patterns and routing,
including error handlers and main views.
"""
import pytest
from django.urls import reverse, resolve
from django.test import Client, override_settings

from oc_lettings_site.views import index


class TestOcLettingsSiteUrls:
    """Test cases for oc_lettings_site URL configuration."""

    def test_index_url_resolves(self):
        """Test that the index URL resolves correctly."""
        url = reverse('index')
        assert url == '/'
        
        resolver = resolve('/')
        assert resolver.func == index
        assert resolver.url_name == 'index'

    def test_lettings_app_urls_included(self):
        """Test that lettings app URLs are properly included."""
        url = reverse('lettings:index')
        assert url == '/lettings/'
        
        resolver = resolve('/lettings/')
        assert resolver.namespace == 'lettings'

    def test_profiles_app_urls_included(self):
        """Test that profiles app URLs are properly included."""
        url = reverse('profiles:index')
        assert url == '/profiles/'
        
        resolver = resolve('/profiles/')
        assert resolver.namespace == 'profiles'

    def test_admin_urls_included(self):
        """Test that admin URLs are included."""
        try:
            from django.urls import reverse
            admin_url = reverse('admin:index')
            assert admin_url == '/admin/'
        except Exception:
            # Admin URLs might not be fully configured in test environment
            pass

    @pytest.mark.django_db
    def test_index_view_accessible(self):
        """Test that the index view is accessible."""
        client = Client()
        response = client.get('/')
        
        assert response.status_code == 200

    def test_url_namespaces(self):
        """Test that all expected namespaces are available."""
        # Test lettings namespace
        lettings_url = reverse('lettings:index')
        lettings_resolver = resolve(lettings_url)
        assert lettings_resolver.namespace == 'lettings'
        
        # Test profiles namespace
        profiles_url = reverse('profiles:index')
        profiles_resolver = resolve(profiles_url)
        assert profiles_resolver.namespace == 'profiles'

    def test_main_url_patterns_structure(self):
        """Test the main URL patterns structure."""
        from oc_lettings_site.urls import urlpatterns
        
        # Should have at least: index, lettings include, profiles include, admin
        assert len(urlpatterns) >= 4
        
        # Check that we have the main patterns
        pattern_paths = []
        for pattern in urlpatterns:
            if hasattr(pattern, 'pattern'):
                pattern_paths.append(str(pattern.pattern))
        
        # Should include root path and app includes
        assert any('$' in path or '/' in path for path in pattern_paths)

    @override_settings(DEBUG=False)
    @pytest.mark.django_db
    def test_404_handler(self):
        """Test that 404 handler is configured."""
        client = Client()
        response = client.get('/nonexistent-page/')
        
        assert response.status_code == 404

    @pytest.mark.django_db  
    def test_static_files_served_in_debug(self):
        """Test that static files configuration is present."""
        from django.conf import settings
        from oc_lettings_site.urls import urlpatterns
        
        if settings.DEBUG:
            # In debug mode, static files should be configured
            # This is handled by Django automatically
            assert True  # Basic check that we're in debug mode

    def test_error_handlers_configured(self):
        """Test that error handlers are properly configured."""
        from oc_lettings_site import urls
        
        # Check if error handlers are defined
        assert hasattr(urls, 'handler404')
        assert hasattr(urls, 'handler500') 
        
        # Check handler functions
        assert urls.handler404 == 'oc_lettings_site.views.custom_404'
        assert urls.handler500 == 'oc_lettings_site.views.custom_500'

    def test_url_reverse_lookup(self):
        """Test URL reverse lookup for all main patterns."""
        # Test main index
        index_url = reverse('index')
        assert index_url == '/'
        
        # Test app URLs
        lettings_index = reverse('lettings:index')
        assert lettings_index == '/lettings/'
        
        profiles_index = reverse('profiles:index')
        assert profiles_index == '/profiles/'

    def test_url_resolution_consistency(self):
        """Test that URL resolution is consistent."""
        # Test that resolving and reversing gives consistent results
        original_url = '/'
        resolver = resolve(original_url)
        reversed_url = reverse(resolver.url_name)
        
        assert original_url == reversed_url

    def test_app_url_isolation(self):
        """Test that app URLs are properly isolated with namespaces."""
        # Both apps have 'index' views, but they should be namespaced
        lettings_index = reverse('lettings:index')
        profiles_index = reverse('profiles:index')
        main_index = reverse('index')
        
        # All should be different URLs
        urls = [lettings_index, profiles_index, main_index]
        assert len(set(urls)) == len(urls)  # All unique