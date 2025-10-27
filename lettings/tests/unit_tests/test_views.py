import pytest
from unittest.mock import patch
from lettings.models import Letting, Address
from lettings.views import index, letting
from django.test import RequestFactory

@pytest.mark.django_db
def test_index_view():
    address = Address.objects.create(
        number=123,
        street="Road",
        city="City",
        state="State",
        zip_code=12,
        country_iso_code=123
    )
    letting = Letting.objects.create(title="Title", address=address)
    request = RequestFactory().get('/lettings/')

    response = index(request)

    assert response.status_code == 200
    content = response.content.decode()

    assert "Title" in content

@pytest.mark.django_db
def test_index_view_exception(caplog):
    request = RequestFactory().get('/lettings/')
    with patch('lettings.views.Letting.objects.all',
               side_effect=Exception("DB error")):
        response = index(request)

    assert response.status_code == 200
    html_content = response.content.decode()
    assert "Lettings" in html_content

    assert any(
        "Erreur lors de la récupération des lettings" in rec.message for rec in
        caplog.records)


@pytest.mark.django_db
def test_letting_view():
    address = Address.objects.create(
        number=123,
        street="Road",
        city="City",
        state="State",
        zip_code=12,
        country_iso_code=123
    )
    letting_obj = Letting.objects.create(title="Title", address=address)
    request = RequestFactory().get(f'/lettings/{letting_obj.id}/')

    response = letting(request, letting_id=letting_obj.id)

    assert response.status_code == 200
    content = response.content.decode()
    assert 'Title' in content
    assert str(address) in content

@pytest.mark.django_db
def test_letting_view_not_found(caplog):
    request = RequestFactory().get('/lettings/999/')
    response = letting(request, letting_id=999)  # ID qui n'existe pas

    assert response.status_code == 404
    html = response.content.decode()
    assert "Page non trouvée" in html  # vérifier que le template 404 est utilisé
    assert any("non trouvé" in rec.message for rec in caplog.records)

@pytest.mark.django_db
def test_letting_view_exception(caplog):
    request = RequestFactory().get('/lettings/1/')

    # Forcer une exception générale sur Letting.objects.get
    with patch('lettings.views.Letting.objects.get', side_effect=Exception("DB error")):
        response = letting(request, letting_id=1)

    assert response.status_code == 500
    html = response.content.decode()
    assert "Erreur serveur" in html
    assert any("Erreur lors de la récupération des lettings" in rec.message for rec in caplog.records)