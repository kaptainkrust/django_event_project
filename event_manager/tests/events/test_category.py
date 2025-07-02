import pytest 
from django.urls import reverse 
from rest_framework import status
from events.models import Category


CATEGORY_CREATE_URL = reverse("category_list_create")


@pytest.mark.django_db
def test_create_category(api_client):
    """Teste das Anlegen einer Kategorie."""

    payload = {
        "name": "abc",
        "sub_title": "Sub Title",
        "description": "Description der Category"
    }

    response = api_client.post(CATEGORY_CREATE_URL, payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert Category.objects.filter(name=payload["name"]).exists()


@pytest.mark.django_db
def test_create_category_same_name_fail(api_client, category):
    payload = {
        "name": category.name,
        "sub_title": "Sub Title",
        "description": "Description der Category"
    }
    response = api_client.post(CATEGORY_CREATE_URL, payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_list_events(token_authenticated_api_client):
    url = reverse("event_list_create")
    client, user = token_authenticated_api_client
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK