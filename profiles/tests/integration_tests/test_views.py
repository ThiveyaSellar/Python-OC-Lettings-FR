import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile

@pytest.mark.django_db
def test_index_view(client):
    # Création d'un utilisateur
    user = User.objects.create(username="testuser")
    # Création d'un profile
    profile = Profile.objects.create(
        user=user,
        favorite_city="Paris"
    )

    url = reverse('profiles:index')
    response = client.get(url)

    assert response.status_code == 200
    assert profile in response.context['profiles_list']

@pytest.mark.django_db
def test_profile_view(client):
    # Création d'un utilisateur
    user = User.objects.create(username="testuser")
    # Création d'un profile
    profile = Profile.objects.create(
        user=user,
        favorite_city="Paris"
    )
    url = reverse('profiles:profile', kwargs={'username': "testuser"})
    response = client.get(url)

    assert response.status_code == 200

    assert response.context['profile'] == profile