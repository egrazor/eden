from .models import Event, Resource
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ()


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        exclude = ()