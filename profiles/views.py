"""
------------------
profiles.views.py
------------------
This module contains the views related to user profiles in the application.
It provides pages to display a list of user profiles and the detailed view of a single profile.
"""
from django.shortcuts import render
from profiles.models import Profile
import logging

logger = logging.getLogger(__name__)

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
    try:
        profiles_list = Profile.objects.all()
    except Exception as e:
        logger.error(f"Erreur lors de ma récupération des profiles: {e}")
        profiles_list = []
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
    try:
        profile = Profile.objects.get(user__username=username)
        logger.info(f"Affichage du profile de: {username}")
    except Profile.DoesNotExist:
        logger.error(f"Profile de {username} non trouvé.")
        return render(request, '404.html', status=404)
    except Exception as e:
        logger.error(
            f"Erreur lors de la récupération du profile de {username} : {e}",
            exc_info=True
        )
        return render(request, '500.html', status=500)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
