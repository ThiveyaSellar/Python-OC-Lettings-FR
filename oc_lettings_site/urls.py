from django.contrib import admin
from django.urls import path, include

from . import views


def trigger_500(request):
    return 1/0


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace="lettings")),
    path('profiles/', include('profiles.urls', namespace="profiles")),
    path('admin/', admin.site.urls),
    path('test-500/', trigger_500),
]
