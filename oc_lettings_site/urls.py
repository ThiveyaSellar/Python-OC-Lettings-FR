from django.contrib import admin
from django.urls import path, include

from . import views


def test_error(request):
    try:
        division_by_zero = 1 / 0
        print(division_by_zero)
    except ZeroDivisionError as e:
        sentry_sdk.capture_exception(
            e)  # Envoie l'exception à Sentry manuellement
        print("Endgame")


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace="lettings")),
    path('profiles/', include('profiles.urls', namespace="profiles")),
    path('admin/', admin.site.urls),
    path('test-error/', test_error),
]
