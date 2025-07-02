"""
User App Urls
"""

from django.urls import path

from .views import hello

urlpatterns = [
    # 1. Argument: der Name der Route
    path("hello-world", hello, name="hello_route"),
]
