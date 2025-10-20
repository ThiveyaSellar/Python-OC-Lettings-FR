"""
------------------
profiles.views.py
------------------
This module contains the views related to user profiles in the application.
It provides pages to display a list of user profiles and the detailed view of a single profile.
"""
from django.shortcuts import render
from profiles.models import Profile


def index(request):
    """
    Return the page with the list of profiles.

    Parameters:
        request (django.http.HttpRequest):
        Http request object with the current request from the user.

    Returns:
        django.http.HttpResponse:
        Rendered HTML page showing the list of profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Return the page displaying the details of a specific user profile.

    Parameters:
        request (django.http.HttpRequest):
            The HTTP request object representing the current request from the user.
        username (string):
            The unique identifier of a user to display.

    Returns:
        django.http.HttpResponse:
            The rendered HTML page showing the profile of the specified user.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
