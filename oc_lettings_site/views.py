"""
Main views module for the OC Lettings Site application.

This module contains the core views of the application, including the home page
and custom error handlers for improved user experience.

The views handle:
- Home page rendering with navigation to lettings and profiles
- Custom 404, 500, and 403 error pages with user-friendly messaging
- Error testing views for development purposes
"""
from django.shortcuts import render


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
    return render(request, 'index.html')


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
    return render(request, '500.html', status=500)
