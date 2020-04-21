from django.urls import path, include

from rest_framework import routers

from . import views

app_name = 'fullcalendar'

router = routers.DefaultRouter()
router.register('events', views.EventViewSet, basename="events")

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),

    path('all_events/', views.EventsView.as_view(), name="all_events"),
    path('add_event/', views.add_event, name="add_event"),
]