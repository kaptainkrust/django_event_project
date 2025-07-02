from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Category, Event

from .serializers import CategoryOutgoingSerializer, CategorySerializer, HelloSerializer


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
