from django.urls import path, include


from . import views

urlpatterns = [
    path('cources/', views.index, name='index')
]

