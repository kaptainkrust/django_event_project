from django.db import transaction

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from events.models import Category, Event


class BulkEventSerializer(serializers.ListSerializer):

    def create(self, validated_data):
        # print("create Bulk")
        events = [Event(**item) for item in validated_data]
        with transaction.atomic():
            Event.objects.bulk_create(events)
            return events



class EventSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Event
        fields = (
            "author",
            "name",
            "sub_title",
            "category",
            "date",
            "min_group",
            "description"
        )
        list_serializer_class = BulkEventSerializer

    def create(self, validated_data):
        print("Validated data eines Events:", validated_data)
        return super().create(validated_data)


class HelloSerializer(serializers.Serializer):
    """Dummy Serializer für Anschauungszwecke."""

    message = serializers.CharField()
    name = serializers.CharField()

    def validate_message(self, value):
        """
        Schema der Validerungmethoden: validate_<FELDNAME>
        """
        if len(value) < 3:
            raise ValidationError("Die Message ist zu kurz.")
        return value.upper()


class EventInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("author", "name")

    author = serializers.StringRelatedField()  # löst die ID auf "bob"


class CategorySerializer(serializers.ModelSerializer):
    """ModelSerializer baut auf dem spezifischen Model auf."""

    events = EventInlineSerializer(many=True, read_only=True)  # related_name
    # events = serializers.PrimaryKeyRelatedField(many=True, queryset=Event.objects.all())

    class Meta:
        model = Category
        fields = "__all__"  # alle Felder


class CategoryOutgoingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")
