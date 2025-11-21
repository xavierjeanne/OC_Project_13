"""
Main views module for the OC Lettings Site application.

This module contains the core views of the application, including the home page
and custom error handlers for improved user experience.

The views handle:
- Home page rendering with navigation to lettings and profiles
- Custom 404, 500, and 403 error pages with user-friendly messaging
- Error testing views for development purposes
"""
import logging
from django.shortcuts import render

# Configure logger for this module
logger = logging.getLogger(__name__)


def index(request):
    """
    Render the main home page of the OC Lettings Site application.

    This view displays the welcome page with navigation links to the main
    sections of the application (lettings and profiles).

    Args:
        request (HttpRequest): The Django HTTP request object containing
                             metadata about the request.

    Returns:
        HttpResponse: Rendered HTML response with the home page template.
                     Status code 200 (OK) on success.
    """
    try:
        # Log access to the main homepage
        client_ip = request.META.get('REMOTE_ADDR', 'unknown')
        user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
        referer = request.META.get('HTTP_REFERER', 'direct')

        logger.info(f"Homepage accessed: IP={client_ip}, Referer={referer}")
        logger.debug(f"Homepage User-Agent: {user_agent}")

        # Log successful homepage rendering
        logger.info("Homepage rendered successfully")
        return render(request, 'index.html')

    except Exception as e:
        # Log any unexpected errors in homepage
        logger.error(f"Unexpected error in homepage view: {str(e)}", exc_info=True)
        raise


def custom_404(request, exception):
    """
    Handle 404 errors with a custom user-friendly page.

    This view is automatically called by Django when a requested URL
    is not found (404 error). It displays a custom error page with
    navigation options instead of the default Django 404 page.

    Args:
        request (HttpRequest): The Django HTTP request object.
        exception (Http404): The exception that triggered the 404 error,
                           containing details about the missing resource.

    Returns:
        HttpResponse: Rendered HTML response with custom 404 error page.
                     Status code 404 (Not Found).
    """
    # Log 404 errors with detailed context
    client_ip = request.META.get('REMOTE_ADDR', 'unknown')
    requested_url = request.get_full_path()
    referer = request.META.get('HTTP_REFERER', 'unknown')
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')

    logger.warning(f"404 Error: URL='{requested_url}', IP={client_ip}, "
                   f"Referer='{referer}', Exception='{exception}'")
    logger.debug(f"404 User-Agent: {user_agent}")

    return render(request, '404.html', status=404)


def custom_500(request):
    """
    Handle 500 errors with a custom user-friendly page.

    This view is automatically called by Django when an internal server
    error occurs (500 error). It displays a custom error page with
    user-friendly messaging and navigation options.

    Args:
        request (HttpRequest): The Django HTTP request object.

    Returns:
        HttpResponse: Rendered HTML response with custom 500 error page.
                     Status code 500 (Internal Server Error).
    """
    # Log 500 errors with detailed context
    client_ip = request.META.get('REMOTE_ADDR', 'unknown')
    requested_url = request.get_full_path()
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')

    logger.error(f"500 Internal Server Error: URL='{requested_url}', IP={client_ip}")
    logger.debug(f"500 User-Agent: {user_agent}")

    return render(request, '500.html', status=500)


def custom_403(request, exception):
    """
    Handle 403 errors with a custom user-friendly page.

    This view is automatically called by Django when access is forbidden
    (403 error). It displays a custom error page with user-friendly
    messaging and navigation options.

    Args:
        request (HttpRequest): The Django HTTP request object.
        exception (PermissionDenied): The exception that triggered the 403 error.

    Returns:
        HttpResponse: Rendered HTML response with custom 403 error page.
                     Status code 403 (Forbidden).
    """
    # Log 403 errors with detailed context
    client_ip = request.META.get('REMOTE_ADDR', 'unknown')
    requested_url = request.get_full_path()
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')

    logger.warning(f"403 Forbidden: URL='{requested_url}', IP={client_ip}, "
                   f"Exception='{exception}'")
    logger.debug(f"403 User-Agent: {user_agent}")

    return render(request, '403.html', status=403)
