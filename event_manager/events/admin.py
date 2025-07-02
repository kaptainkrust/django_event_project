from django.contrib import admin

from .models import Category, Event


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "sub_title", "number_events"]
    list_display_links = ["id", "name"]  # klickbar
    search_fields = ["name", "sub_title"]  # Suchbox sucht in Name und Subtitle

    def number_events(self, instance) -> int:
        return instance.events.count()


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "sub_title", "category"]
    list_display_links = ["id", "name"]  # klickbar
    search_fields = ["name", "sub_title"]  # Suchbox sucht in Name und Subtitle
