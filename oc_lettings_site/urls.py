from django.contrib import admin
from django.urls import path, include

from . import views


def test_error(request):
    division_by_zero = 1 / 0
    print(division_by_zero)


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace="lettings")),
    path('profiles/', include('profiles.urls', namespace="profiles")),
    path('admin/', admin.site.urls),
    path('test-error/', test_error),
]
