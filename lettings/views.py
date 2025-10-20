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
    lettings_list = Letting.objects.all()
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
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
