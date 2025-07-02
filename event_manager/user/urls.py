"""
User App Urls

admin user token: c67ea25db1e0a135086f13a87f6f407169aef4b6
"""

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import hello

urlpatterns = [
    # 1. Argument: der Name der Route
    path("hello-world", hello, name="hello_route"),

    # curl -X POST http://127.0.0.1:8000/user/token -d "username=admin&password=abcd1234"
    path("token", obtain_auth_token, name="api-token"),  # POST
]
