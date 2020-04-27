from django.urls import path
from django.contrib.auth.views import auth_login

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.index, name="index"),
    path('logout/', views.logout, name='logout'),
    path('authenticate/', views.login, name='login'),
    path('register/', views.register, name='register')
]