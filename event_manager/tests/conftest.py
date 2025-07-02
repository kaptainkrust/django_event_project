import pytest 

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from events.factories import CategoryFactory 
from user.factories import UserFactory

@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def category():
    return CategoryFactory()


@pytest.fixture
def token_authenticated_api_client():
    user = UserFactory()
    token = Token.objects.create(user=user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
    return client, user
