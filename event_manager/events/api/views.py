import logging
from django.db import transaction
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework import generics, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from events.models import Category, Event

from .serializers import (CategoryOutgoingSerializer, 
                          CategorySerializer, 
                          HelloSerializer, 
                          EventSerializer,
                          )



logger = logging.getLogger(__name__)


class EventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)


class EventListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.prefetch_related("author")

    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    # Um die Suche zu implementieren, filter.SearchFilter aus DRF 
    # angeben
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,  # zum Sortieren bei der Ausgabe
    ]

    # http://127.0.0.1:8000/api/events/event?search=xy
    # name => full text
    # =name => extact search
    # $name => REGEX Suche (POSTGRES)
    # ^name => starts-with suche
    search_fields = ["name", "=sub_title", "^category__name"]

    # http://127.0.0.1:8000/api/events/event?search=xy
    ordering_fields = ["date", "name"]

    @method_decorator(cache_page(60))  # 60 SEKUNDEN CACHE
    def list(self, request, *args, **kwargs):
        """Auflisten aller Events."""
        return super().list(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        """
        FAlls eine Liste übergeben wird, muss der Serializer mit 
        many=True aufgerufen werden.
        """
        data = kwargs.get("data")
        if isinstance(data, list):
            kwargs["many"] = True
        return super().get_serializer(*args, **kwargs)

    def perform_create(self, serializer):
        """
        Wird aufgerufen, wenn ein Objekt erstellt wird. Wird nur ausgeführt, wenn 
        die Daten bei Eingabe valide sind.
        """
        logger.info("Info messsage")
        logger.debug("Debug Message")
        logger.warning("Warning")

        if not self.request.user.is_authenticated:
            raise NotAuthenticated("User muss authentifiziert sein.")
        
        user = self.request.user

        # eingehdnen Daten anreichern mit Zusatzinformation
        if isinstance(serializer.validated_data, list):
            for item in serializer.validated_data:
                item["author"] = user 
        else:
            serializer.validated_data["author"] = user 
        
        serializer.save()

        # self.validated_data beinhaltet die schon validiert daten
        # durch serializer.is_valid(raise_exception=True)
       
         # keine Validierung!!!!



class HelloView(APIView):
    def get(self, request) -> Response:
        """
        GET: Daten holen
        curl -X GET http://127.0.0.1/api/events/hello
        """
        data = {"message": "Test Message", "name": "Bob"}
        serializer = HelloSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        """
        POST: Daten via Post senden
        curl -X POST http://127.0.0.1:8000/api/events/hello
        -H "Content-Type: application/json"
        -d '{"message": "hi there", "name": "Alice"}'
        """
        serializer = HelloSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # erstellt ein dict namens validated_data
        print(serializer.validated_data)  # z.b. erstellen eines neuen Objekts
        print(serializer.data)  # für die Rückgabe via Response
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    """View zum Anlegen und Auflisten von Kategorien."""

    serializer_class = CategorySerializer
    queryset = Category.objects.prefetch_related("events", "events__author")  # Inner Join
    # man kann auch raw-SQL nutzen:
    # Category.objects.raw("SELECT * FROM categories LEFT JOIN on ..."):


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """View zum Holen, Updaten oder Löschen einer Kategorie."""

    serializer_class = CategorySerializer
    queryset = Category.objects.prefetch_related("events", "events__author")

    def update(self, request, *args, **kwargs):
        """Die Update-Methode füR PUT Request überschreiben, um anderen
        Rückgabe-Serializer zu nutzen.
        """
        category = self.get_object()
        print(f"Das Kategorie-Objekt, welches upgedated wird: {category}")
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)  # erstellt das validated dict
        serializer.save()

        # nutzen wir anderen Serializer für die Rückgabe
        response_serializer = CategoryOutgoingSerializer(serializer.instance)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        category = self.get_object()
        print(f"Das Kategorie-Objekt, welches upgedated wird: {category}")
        serializer = CategorySerializer(category, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)  # erstellt das validated dict
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
