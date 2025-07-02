"""
Dieses Subkommando erstellt neue Events
"""

from django.core.management.base import BaseCommand

from events.factories import EventFactory
from events.models import Category, Event


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "-n",
            "--number",
            help="Anzahl der Events die angelegt werden",
            required=True,
            type=int,
        )
        parser.epilog = "Usage: python manage.py create_events --number 10"

    def handle(self, *args, **kwargs):
        number = kwargs.get("number")  # --number
        print("Lösche Kategorien und Events..")

        # für den Fall, dass on_delete PROTECTED/RESTRICTED wäre
        for model in Event, Category:
            model.objects.all().delete()

        print(f"Lege neue Events an: {number}")
        generated_events = EventFactory.create_batch(number)
        print(generated_events)

        # EventFactory(author=bob, category=sport)
