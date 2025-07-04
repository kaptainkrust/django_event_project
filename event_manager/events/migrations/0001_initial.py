# Generated by Django 5.2.3 on 2025-06-30 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, unique=True)),
                ("sub_title", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="Beschreibung der Kategorie", null=True
                    ),
                ),
                ("active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, unique=True)),
                ("sub_title", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="Beschreibung der Kategorie", null=True
                    ),
                ),
                ("date", models.DateTimeField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events",
                        to="events.category",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
