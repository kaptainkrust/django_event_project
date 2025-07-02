# PROJEKT URLs
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    path("api/events/", include("events.api.urls")),
]

if settings.DEBUG:
    # Wenn wir im DEBUG Modus sind (DEBUG=True) wird die
    # Debug Toolbar genutzt
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
