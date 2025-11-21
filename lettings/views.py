"""
Views module for the lettings application.

This module handles the display and management of letting properties,
providing both list and detail views for users to browse available
rental properties and their associated address information.

Functions:
    index: Display a list of all available lettings
    letting: Display detailed information for a specific letting
"""
from django.shortcuts import render, get_object_or_404
from .models import Letting


def index(request):
    """
    Display a list of all available lettings.

    This view retrieves all letting objects from the database and renders
    them in a list format, allowing users to browse available properties
    and navigate to detailed views.

    Args:
        request (HttpRequest): The Django HTTP request object containing
                             metadata about the request.

    Returns:
        HttpResponse: Rendered HTML response displaying the lettings list.
                     Includes context with 'lettings_list' containing all
                     Letting objects ordered by default model ordering.
                     Status code 200 (OK) on success.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Display detailed information for a specific letting.

    This view retrieves and displays comprehensive information about a single
    letting property, including its title and complete address details.
    Returns a 404 error if the letting does not exist.

    Args:
        request (HttpRequest): The Django HTTP request object.
        letting_id (int): The primary key ID of the letting to display.
                         Must be a positive integer corresponding to an
                         existing Letting object.

    Returns:
        HttpResponse: Rendered HTML response with letting details.
                     Includes context with 'title' and 'address' data.
                     Status code 200 (OK) on success.

    Raises:
        Http404: If no Letting object with the specified ID exists.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
