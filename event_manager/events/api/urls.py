"""
Api URLS der Event Api
"""

from django.urls import path

from .views import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    HelloView,
    EventListCreateAPIView,
    EventRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    # api/events/event
    path("event", EventListCreateAPIView.as_view(), name="event_list_create"),
    path("event/<int:pk>", EventRetrieveUpdateDestroyAPIView.as_view(), name="event_updat"),
    # /api/events/hello/
    path("hello", HelloView.as_view(), name="hello_api"),
    # /api/events/category (zum Auflisten und Anlegen)
    path("category", CategoryListCreateAPIView.as_view(), name="category_list_create"),
    path(
        "category/<int:pk>",
        CategoryRetrieveUpdateDestroyAPIView.as_view(),
        name="category_update_destroy",
    ),
]
