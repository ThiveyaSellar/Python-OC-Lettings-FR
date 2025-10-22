import pytest

from django.urls import reverse, resolve
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_url():
    # Création d'un utilisateur
    user = User.objects.create(username="testuser")
    # Création d'un profile
    Profile.objects.create(
        user=user,
        favorite_city="Paris"
    )
    path = reverse('profiles:profile', kwargs={'username': "testuser"})

    assert path == "/profiles/testuser/"
    assert resolve(path).view_name == "profiles:profile"

def test_profile_index_url():
    path = reverse('profiles:index')
    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles:index"
