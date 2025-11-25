from django.contrib import admin
from django.urls import path, include

from . import views
import logging


logger = logging.getLogger(__name__)


def test_error(request):
    print("dada")


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace="lettings")),
    path('profiles/', include('profiles.urls', namespace="profiles")),
    path('admin/', admin.site.urls),
    path('test-error/', test_error),
]
