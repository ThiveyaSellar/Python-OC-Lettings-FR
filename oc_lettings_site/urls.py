from django.contrib import admin
from django.urls import path, include

from . import views
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def test_error(request):
    try:
        division_by_zero = 1 / 0
    except ZeroDivisionError:
        logger.exception("Une erreur de division par zéro a été capturée et envoyée à Sentry.")
        return HttpResponse("Erreur capturée et envoyée à Sentry via le logger.")

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace="lettings")),
    path('profiles/', include('profiles.urls', namespace="profiles")),
    path('admin/', admin.site.urls),
    path('test-error/', test_error),
]
