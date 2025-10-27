import pytest
from django.test import RequestFactory
from django.contrib.auth.models import User
from profiles.models import Profile
from profiles.views import index, profile

@pytest.mark.django_db
def test_index_view():
    user = User.objects.create(username="testuser")
    profile_obj = Profile.objects.create(user=user, favorite_city="Paris")

    request = RequestFactory().get('/profiles/')

    response = index(request)

    assert response.status_code == 200
    html = response.content.decode()
    assert "testuser" in html

@pytest.mark.django_db
def test_profile_view():
    user = User.objects.create(username="testuser")
    profile_obj = Profile.objects.create(user=user, favorite_city="Paris")

    request = RequestFactory().get(f'/profiles/{user.username}/')

    response = profile(request, username=user.username)

    assert response.status_code == 200
    html = response.content.decode()
    assert "testuser" in html
    assert "Paris" in html