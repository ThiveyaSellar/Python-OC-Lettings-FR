"""
------------------
lettings.views.py
------------------
This module contains the views related to lettings in the application.
It provides pages to display a list of lettings and the details of a specific letting.

Functions:
    index(request) -> HttpResponse
    letting(request, letting_id) -> HttpResponse
"""

from django.shortcuts import render
from lettings.models import Letting
import logging

logger = logging.getLogger(__name__)

def index(request):
    """
    Return the page with the list of lettings.

    Parameters:
        request (django.http.HttpRequest):
        Http request object with the current request from the user.

    Returns:
        django.http.HttpResponse:
        Rendered HTML page showing the list of lettings.
    """
    try:
        lettings_list = Letting.objects.all()
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des lettings: {e}")
        lettings_list = []
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Return the page displaying the details of a specific letting.

    Parameters:
        request (django.http.HttpRequest):
            The HTTP request object representing the current request from the user.
        letting_id (int):
            The unique identifier of the letting to display.

    Returns:
        django.http.HttpResponse:
            The rendered HTML page showing the details of the specified letting.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        logger.info(f"Affichage du letting id={letting_id}: {letting.title}")
    except Letting.DoesNotExist:
        logger.error(f"Letting id={letting_id} non trouvé")
        return render(request, '404.html', status=404)
    except Exception as e:
        logger.error(
            f"Erreur lors de la récupération des lettings: {e}",
            exc_info=True
        )
        return render(request, "500.html", status=500)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)

def test_error(request):
    division_by_zero = 1 / 0
