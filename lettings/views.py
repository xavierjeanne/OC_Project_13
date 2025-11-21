"""
Views module for the lettings application.

This module handles the display and management of letting properties,
providing both list and detail views for users to browse available
rental properties and their associated address information.

Functions:
    index: Display a list of all available lettings
    letting: Display detailed information for a specific letting
"""
import logging
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Letting

# Configure logger for this module
logger = logging.getLogger(__name__)


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
    try:
        # Log the access to lettings index page
        client_ip = request.META.get('REMOTE_ADDR', 'unknown')
        user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
        logger.info(f"Lettings index accessed from IP: {client_ip}, User-Agent: {user_agent}")

        lettings_list = Letting.objects.all()
        lettings_count = lettings_list.count()

        # Log the number of lettings returned
        logger.debug(f"Retrieved {lettings_count} lettings for index page")

        context = {'lettings_list': lettings_list}

        # Log successful response
        logger.info(f"Lettings index page rendered successfully with {lettings_count} lettings")
        return render(request, 'lettings/index.html', context)

    except Exception as e:
        # Log any unexpected errors
        logger.error(f"Unexpected error in lettings index view: {str(e)}", exc_info=True)
        raise


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
    try:
        # Log the access attempt with critical parameters
        client_ip = request.META.get('REMOTE_ADDR', 'unknown')
        logger.info(f"Letting detail accessed: ID={letting_id}, IP={client_ip}")

        # Attempt to get the letting - this may raise Http404
        letting = get_object_or_404(Letting, id=letting_id)

        # Log successful retrieval with letting details
        logger.info(f"Letting found: ID={letting_id}, Title='{letting.title}', "
                    f"Address='{letting.address}'")

        context = {
            'title': letting.title,
            'address': letting.address,
        }

        # Log successful rendering
        logger.debug(f"Letting detail page rendered successfully for ID={letting_id}")
        return render(request, 'lettings/letting.html', context)

    except Http404:
        # Log 404 errors with relevant information
        logger.warning(f"Letting not found: ID={letting_id}, IP={client_ip}")
        raise

    except Exception as e:
        # Log any unexpected errors with full context
        logger.error(f"Unexpected error in letting detail view: ID={letting_id}, "
                     f"Error={str(e)}", exc_info=True)
        raise
