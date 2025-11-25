from django.contrib import admin
from django.urls import path, include

from . import views
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def test_error(request):
    try:
        division_by_zero = 1 / 0
        print(division_by_zero)
    except ZeroDivisionError:
        logger.exception("Une erreur  Sentry.")
        return HttpResponse("Erreur capturée et envoyée à .")


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace="lettings")),
    path('profiles/', include('profiles.urls', namespace="profiles")),
    path('admin/', admin.site.urls),
    path('test-error/', test_error),
]
