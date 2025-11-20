from django.urls import reverse, resolve


def test_index_url():
    path = reverse('index')
    assert path == "/"
    assert resolve(path).view_name == "index"
