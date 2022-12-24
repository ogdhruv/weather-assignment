from weather.models import City
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    """A modelSerializer for for converting the complex queryset representation into
    python friendly dictionary.

    Args:
        serializers (class): ModelSerializer
    """
    class Meta:
        model = City
        fields = "__all__"
