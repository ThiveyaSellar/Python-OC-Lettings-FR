from django.contrib import admin
from django.urls import path

from . import views

# Ajout namespace
app_name = "profiles"

# Retrait de profiles dans le chemin
# Sinon doublon avec fichier principal urls.py
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
