from django.contrib import admin
from django.urls import path, include

from . import views


def test_error(request):
    try:
        division_by_zero = 1 / 0
    except ZeroDivisionError as e:
        sentry_sdk.capture_exception(
            e)  # Envoie l'exception à Sentry manuellement
        return HttpResponse("Erreur capturée et envoyée à Sentry.")


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace="lettings")),
    path('profiles/', include('profiles.urls', namespace="profiles")),
    path('admin/', admin.site.urls),
    path('test-error/', test_error),
]
