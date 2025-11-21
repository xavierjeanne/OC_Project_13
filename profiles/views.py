"""
Views module for the profiles application.

This module handles the display and management of user profiles,
providing both list and detail views for users to browse registered
users and view their profile information including favorite cities.

Functions:
    index: Display a list of all user profiles
    profile: Display detailed information for a specific user profile
"""
import logging
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Profile

# Configure logger for this module
logger = logging.getLogger(__name__)


def index(request):
    """
    Display a list of all user profiles.
    This view retrieves all profile objects from the database and renders
    them in a list format, allowing users to browse registered users
    and navigate to their detailed profiles.

    Args:
        request (HttpRequest): The Django HTTP request object containing
                             metadata about the request.

    Returns:
        HttpResponse: Rendered HTML response displaying the profiles list.
                     Includes context with 'profiles_list' containing all
                     Profile objects ordered by default model ordering.
                     Status code 200 (OK) on success.
    """
    try:
        # Log the access to profiles index page
        client_ip = request.META.get('REMOTE_ADDR', 'unknown')
        user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
        logger.info(f"Profiles index accessed from IP: {client_ip}, User-Agent: {user_agent}")

        profiles_list = Profile.objects.all()
        profiles_count = profiles_list.count()

        # Log the number of profiles returned
        logger.debug(f"Retrieved {profiles_count} profiles for index page")

        context = {'profiles_list': profiles_list}

        # Log successful response
        logger.info(f"Profiles index page rendered successfully with {profiles_count} profiles")
        return render(request, 'profiles/index.html', context)

    except Exception as e:
        # Log any unexpected errors
        logger.error(f"Unexpected error in profiles index view: {str(e)}", exc_info=True)
        raise


def profile(request, username):
    """
    Display detailed information for a specific user profile.

    This view retrieves and displays comprehensive information about a single
    user profile, including username, personal details, and favorite city.
    Returns a 404 error if the profile does not exist.

    Args:
        request (HttpRequest): The Django HTTP request object.
        username (str): The username of the user whose profile to display.
                       Must correspond to an existing User with an associated
                       Profile object.

    Returns:
        HttpResponse: Rendered HTML response with profile details.
                     Includes context with 'profile' containing the Profile
                     object and associated User information.
                     Status code 200 (OK) on success.

    Raises:
        Http404: If no Profile object exists for a User with the specified username.
    """
    try:
        # Log the access attempt with critical parameters
        client_ip = request.META.get('REMOTE_ADDR', 'unknown')
        logger.info(f"Profile detail accessed: username='{username}', IP={client_ip}")

        # Attempt to get the profile - this may raise Http404
        profile = get_object_or_404(Profile, user__username=username)

        # Log successful retrieval with profile details
        logger.info(f"Profile found: username='{username}', "
                    f"User ID={profile.user.id}, "
                    f"Favorite city='{profile.favorite_city}'")

        context = {'profile': profile}

        # Log successful rendering
        logger.debug(f"Profile detail page rendered successfully for username='{username}'")
        return render(request, 'profiles/profile.html', context)

    except Http404:
        # Log 404 errors with relevant information
        logger.warning(f"Profile not found: username='{username}', IP={client_ip}")
        raise

    except Exception as e:
        # Log any unexpected errors with full context
        logger.error(f"Unexpected error in profile detail view: username='{username}', "
                     f"Error={str(e)}", exc_info=True)
        raise
