import pytest
from django.contrib.auth.models import User
from profiles.models import Profile

@pytest.mark.django_db
def test_profile_creation():
    # Création d'un utilisateur
    user = User.objects.create(username="testuser")
    # Création d'un profile
    profile = Profile.objects.create(
        user=user,
        favorite_city="Paris"
    )
    assert str(profile) == 'testuser'
    assert Profile.objects.count() == 1