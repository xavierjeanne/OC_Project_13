"""
Views module for the profiles application.

This module handles the display and management of user profiles,
providing both list and detail views for users to browse registered
users and view their profile information including favorite cities.

Functions:
    index: Display a list of all user profiles
    profile: Display detailed information for a specific user profile
"""
from django.shortcuts import render, get_object_or_404
from .models import Profile


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
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


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
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
