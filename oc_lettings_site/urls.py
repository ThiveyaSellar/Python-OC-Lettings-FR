from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from . import views
import sentry_sdk


def test_error(request):
    try:
        division_by_zero = 1 / 0
        print(division_by_zero)
    except ZeroDivisionError as e:
        sentry_sdk.capture_exception(e)  # Envoie
        return HttpResponse("Erreur capturée et envoyée à Sentry.")


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace="lettings")),
    path('profiles/', include('profiles.urls', namespace="profiles")),
    path('admin/', admin.site.urls),
]
