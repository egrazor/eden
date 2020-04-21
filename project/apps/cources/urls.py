from django.urls import path, include


from . import views

app_name = 'cources'

urlpatterns = [
    path('', views.index, name='index')
]

