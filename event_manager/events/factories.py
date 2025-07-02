from datetime import timedelta
import random

from django.utils import timezone
import factory

from user.factories import UserFactory

from . import models

categories = [
    "Sports",
    "Radio",
    "Kultur",
]


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category
        django_get_or_create = ("name",)

    name = factory.Iterator(categories)
    sub_title = factory.Faker("sentence")
    description = factory.Faker("paragraph", nb_sentences=3)


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Event

    name = factory.Faker("sentence")
    sub_title = factory.Faker("sentence")
    description = factory.Faker("paragraph", nb_sentences=3)
    min_group = factory.LazyAttribute(
        lambda _: random.choice(list(models.Event.Group.values))
    )
    date = factory.Faker(
        "date_time_between",
        start_date=timezone.now() + timedelta(days=1),
        end_date=timezone.now() + timedelta(days=60),
        tzinfo=timezone.get_current_timezone(),
    )

    # EventFactory(author=bob, category=sport) überscheibt:
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
