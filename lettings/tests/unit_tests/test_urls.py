import pytest

from django.urls import reverse, resolve
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_letting_url():
    # Création d'une adresse
    address = Address.objects.create(
        number = 123,
        street = "Road",
        city = "City",
        state = "State",
        zip_code = 12,
        country_iso_code = 123
    )
    # Création d'une location associée à cette addresse
    Letting.objects.create(
        title = "Title",
        address = address
    )
    path = reverse('lettings:letting', kwargs={'letting_id': 1})

    assert path == "/lettings/1/"
    assert resolve(path).view_name == "lettings:letting"

def test_letting_index_url():
    path = reverse('lettings:index')
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings:index"
