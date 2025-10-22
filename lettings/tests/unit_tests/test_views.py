import pytest
from django.urls import reverse # à quoi sert reverse
from lettings.models import Letting, Address

@pytest.mark.django_db
def test_index_view(client):
    # Création d'une adresse
    address = Address.objects.create(
        number=123,
        street="Road",
        city="City",
        state="State",
        zip_code=12,
        country_iso_code=123
    )
    # Création d'une location associée à cette addresse
    letting = Letting.objects.create(
        title="Title",
        address=address
    )

    url = reverse('lettings:index')
    response = client.get(url)

    assert response.status_code == 200
    assert letting in response.context['lettings_list']

@pytest.mark.django_db
def test_letting_view(client):
    # Création d'une adresse
    address = Address.objects.create(
        number=123,
        street="Road",
        city="City",
        state="State",
        zip_code=12,
        country_iso_code=123
    )
    # Création d'une location associée à cette addresse
    letting = Letting.objects.create(
        title="Title",
        address=address
    )
    url = reverse('lettings:letting', kwargs={'letting_id': letting.id})
    response = client.get(url)

    assert response.status_code == 200

    assert response.context['title'] == letting.title
    assert response.context['address'] == letting.address