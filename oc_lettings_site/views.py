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
    logger.info("Page d’accueil consultée")
    return render(request, 'index.html')
