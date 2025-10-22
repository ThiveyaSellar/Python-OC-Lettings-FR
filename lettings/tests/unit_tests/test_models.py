import pytest
from lettings.models import Address, Letting

@pytest.mark.django_db
def test_address_creation():
    address = Address.objects.create(
        number=123,
        street="Road",
        city="City",
        state="State",
        zip_code=12,
        country_iso_code=123
    )
    assert str(address) == '123 Road'
    assert Address.objects.count() == 1

@pytest.mark.django_db
def test_letting_creation():
    address = Address.objects.create(
        number=123,
        street="Road",
        city="City",
        state="State",
        zip_code=12,
        country_iso_code=123
    )
    letting = Letting.objects.create(
        title="Title",
        address=address
    )
    assert str(letting) == 'Title'
    assert Address.objects.count() == 1
    assert Letting.objects.count() == 1