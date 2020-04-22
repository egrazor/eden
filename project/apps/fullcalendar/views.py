from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics, viewsets

from .models import Event, Resource
from .serializers import EventSerializer, ResourceSerializer


def index(request):
    template_name = 'fullcalendar/fullcalendar.html'
    return render(request, template_name)


def add_event(request):
    return HttpResponse(request.POST)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer