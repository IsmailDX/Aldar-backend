from rest_framework import serializers
from .models import PropertiesDetails


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertiesDetails
        fields = "__all__"
