from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()  # holt aktuelles UserModel


class DateMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # beim Anlegen wird dieser Timestamp
    updated_at = models.DateTimeField(
        auto_now=True
    )  # beim Update der Tabelle wird Timestamp gesetzt

    class Meta:
        abstract = True


class Category(DateMixin):
    """Kategorie eines Events, zb. Sport."""

    # xyz = models.UUID(primary_key=True)
    name = models.CharField(max_length=100, unique=True)  # mandatory
    # blank=True => darf im Formular leer sein
    # null=True => darf nullable sein in der DB
    sub_title = models.CharField(max_length=100, blank=True, null=True)  # optional
    description = models.TextField(
        blank=True, null=True, help_text="Beschreibung der Kategorie"
    )  # optional
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Event(DateMixin):
    """Event Model hat foreign Key auf Category."""

    class Group(models.IntegerChoices):
        SMALL = (5, "kleine Gruppe")
        BIG = (10, "große Gruppe")
        UNLIMITED = (0, "unendlich")

    name = models.CharField(max_length=100, unique=True)  # mandatory
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(
        blank=True, null=True, help_text="Beschreibung der Kategorie"
    )
    date = models.DateTimeField()  # Zeitpunkt des Events
    min_group = models.PositiveSmallIntegerField(
        choices=Group.choices, default=Group.UNLIMITED
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="events"
    )  #  sport.events.all()

    def __str__(self) -> str:
        return self.name
