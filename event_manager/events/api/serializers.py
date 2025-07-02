from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from events.models import Category, Event


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
