"""
------------------
oc_lettings_site.views.py
------------------
This module contains the view providing the display of the main page.
"""
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Render the homepage of the application.

    Parameters:
        request (django.http.HttpRequest):
        The HTPP request object representing the current request from the user.

    Returns:
        django.http.HttpResponse:
        The rendered HTML page for the homepage ('index.html').
    """
    logger = logging.getLogger(__name__)
    logger.info("Page d’accueil consultéee")
    return render(request, 'index.html')


def trigger_500_error(request):
    try:
        1 / 0
    except Exception as e:
        logger.error("Erreur serveur, division par zero")
        return render(request, "500.html", status=500)
