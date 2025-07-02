"""
Dieses Subkommando erstellt 3 neue User und
löscht die bestehenden User (exclusive User admin)

Subkommando ausführen

python manage.py create_user
"""

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from user.factories import UserFactory

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Bestehende User löschen...")
        User.objects.exclude(username="admin").delete()

        print("Generiere neue User...")
        users = UserFactory.create_batch(3)

        print(f"Folgende User wurden angelegt: {users}")
