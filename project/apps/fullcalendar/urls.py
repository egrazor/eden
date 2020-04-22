from django.urls import path, include

from rest_framework import routers

from . import views

app_name = 'fullcalendar'

router = routers.DefaultRouter()
router.register('events', views.EventViewSet, basename="events")
router.register('resources', views.ResourceViewSet, basename="resources")

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),

    path('add_event/', views.add_event, name="add_event"),
]