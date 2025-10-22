import pytest

from django.urls import reverse, resolve
from django.contrib.auth.models import User
from profiles.models import Profile


def test_index_url():
    path = reverse('index')
    assert path == "/"
    assert resolve(path).view_name == "index"
