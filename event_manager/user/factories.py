"""
In Factory Boy wird LazyFunction oft genutzt, um dynamische Werte zu erzeugen,
die vom Zustand der Factory abhängen oder mit der aktuellen Zeit zu tun haben.
"""

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
import factory

DEFAULT_PASSWORD = "abc"


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ("username",)

    username = factory.Iterator(["bob", "alice", "john"])
    # password = factory.LazyFunction(lambda: make_password(DEFAULT_PASSWORD))
    password = make_password(DEFAULT_PASSWORD)
    email = factory.Faker("email")
