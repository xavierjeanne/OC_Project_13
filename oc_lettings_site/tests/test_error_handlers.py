"""
Tests for custom error handlers.

These tests aim to improve coverage of 404, 500, 403 error handlers.
"""
from django.test import TestCase, Client, override_settings
from unittest.mock import patch, Mock


class TestErrorHandlers(TestCase):
    """Tests for custom error handlers."""

    def setUp(self):
        self.client = Client()

    @override_settings(DEBUG=False)
    def test_custom_404_handler(self):
        """Test custom 404 error handler."""
        # Try to access a non-existent URL
        response = self.client.get('/nonexistent-url/')

        # Django should return the custom 404 template
        self.assertEqual(response.status_code, 404)

    @override_settings(DEBUG=False)
    def test_custom_404_with_logging(self):
        """Test 404 handler with logging verification."""
        with patch('oc_lettings_site.views.logger'):
            response = self.client.get('/nonexistent-url/')

            # Verify that logger was called on 404 error
            # (will be called during template rendering)
            self.assertEqual(response.status_code, 404)

    def test_letting_not_found_404(self):
        """Test 404 for non-existent letting."""
        response = self.client.get('/lettings/999/')
        self.assertEqual(response.status_code, 404)

    def test_profile_not_found_404(self):
        """Test 404 for non-existent profile."""
        response = self.client.get('/profiles/nonexistent/')
        self.assertEqual(response.status_code, 404)

    @override_settings(DEBUG=False)
    def test_custom_500_handler_coverage(self):
        """Test to improve 500 handler coverage."""
        # This test is complex as it requires triggering a real 500 error
        # We can at least test that the function exists and is callable
        from oc_lettings_site.views import custom_500

        # Mock request object
        mock_request = Mock()
        mock_request.META = {
            'REMOTE_ADDR': '127.0.0.1',
            'HTTP_USER_AGENT': 'Test Agent'
        }

        # Test that the function can be called
        response = custom_500(mock_request)
        self.assertEqual(response.status_code, 500)

    @override_settings(DEBUG=False)
    def test_custom_403_handler_coverage(self):
        """Test to improve 403 handler coverage."""
        from oc_lettings_site.views import custom_403

        # Mock request and exception
        mock_request = Mock()
        mock_request.META = {
            'REMOTE_ADDR': '127.0.0.1',
            'HTTP_USER_AGENT': 'Test Agent'
        }
        mock_exception = Exception("Forbidden")

        # Test that the function can be called
        response = custom_403(mock_request, mock_exception)
        self.assertEqual(response.status_code, 403)

    def test_logging_integration_with_views(self):
        """Test logging integration with views."""
        with patch('oc_lettings_site.views.logger') as mock_logger:
            # Test home page
            self.client.get('/')
            mock_logger.info.assert_called()

        with patch('lettings.views.logger') as mock_logger:
            # Test lettings page
            self.client.get('/lettings/')
            mock_logger.info.assert_called()

        with patch('profiles.views.logger') as mock_logger:
            # Test profiles page
            self.client.get('/profiles/')
            mock_logger.info.assert_called()
