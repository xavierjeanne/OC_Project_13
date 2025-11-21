"""
Additional tests for logging coverage and error handling.

These tests aim to cover the try/except blocks added for logging
in order to improve code coverage.
"""
from django.test import TestCase, Client
from unittest.mock import patch
from django.contrib.auth.models import User
from lettings.models import Address, Letting
from profiles.models import Profile


class TestLoggingCoverage(TestCase):
    """Tests to improve logging code coverage."""

    def setUp(self):
        self.client = Client()

    def test_lettings_index_exception_handling(self):
        """Test exception handling in lettings index."""
        with patch('lettings.views.Letting.objects.all') as mock_all:
            # Simulate an exception during object retrieval
            mock_all.side_effect = Exception("Database error")

            with self.assertRaises(Exception):
                self.client.get('/lettings/')

    def test_lettings_detail_exception_handling(self):
        """Test exception handling in lettings detail."""
        with patch('lettings.views.get_object_or_404') as mock_get:
            # Simulate an exception other than Http404
            mock_get.side_effect = Exception("Database error")

            with self.assertRaises(Exception):
                self.client.get('/lettings/1/')

    def test_profiles_index_exception_handling(self):
        """Test exception handling in profiles index."""
        with patch('profiles.views.Profile.objects.all') as mock_all:
            # Simulate an exception during object retrieval
            mock_all.side_effect = Exception("Database error")

            with self.assertRaises(Exception):
                self.client.get('/profiles/')

    def test_profiles_detail_exception_handling(self):
        """Test exception handling in profiles detail."""
        with patch('profiles.views.get_object_or_404') as mock_get:
            # Simulate an exception other than Http404
            mock_get.side_effect = Exception("Database error")

            with self.assertRaises(Exception):
                self.client.get('/profiles/testuser/')

    def test_main_index_exception_handling(self):
        """Test exception handling in main view."""
        with patch('oc_lettings_site.views.render') as mock_render:
            # Simulate an exception during render
            mock_render.side_effect = Exception("Template error")

            with self.assertRaises(Exception):
                self.client.get('/')

    def test_custom_error_handlers_coverage(self):
        """Test to cover custom error handlers."""
        from oc_lettings_site.views import custom_404, custom_500, custom_403

        self.assertTrue(callable(custom_404))
        self.assertTrue(callable(custom_500))
        self.assertTrue(callable(custom_403))

    def test_logging_calls_in_views(self):
        """Test that logging calls are properly executed."""

        user = User.objects.create_user(username='testuser')
        Profile.objects.create(user=user, favorite_city='Paris')

        address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='USA'
        )
        Letting.objects.create(title='Test Letting', address=address)

        # Test logging calls with mocks to verify logging is executed
        with patch('lettings.views.logger') as mock_logger:
            self.client.get('/lettings/')
            self.assertTrue(mock_logger.info.called)
            self.assertTrue(mock_logger.debug.called)

        with patch('profiles.views.logger') as mock_logger:
            self.client.get('/profiles/')
            self.assertTrue(mock_logger.info.called)
            self.assertTrue(mock_logger.debug.called)

        with patch('oc_lettings_site.views.logger') as mock_logger:
            self.client.get('/')
            self.assertTrue(mock_logger.info.called)
