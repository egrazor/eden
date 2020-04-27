from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import auth_login, auth_logout
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponse, HttpResponseRedirect

from .forms import RegisterForm


def index(request):
    template_name = 'users/login.html'
    return render(request, template_name)


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect('/')
    else:
        return HttpResponse('Аутентификация не пройдена')


def logout(request):
    auth_logout(request)
    return redirect('/')


def register(request):
    if request.method != 'POST':
        form = RegisterForm()
    else:
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            new_user.set_password(request.POST['password1'])
            new_user.save()
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'],
                                              )
            auth_login(request, authenticated_user)
            return HttpResponseRedirect(reverse('cources:index'))
    context = {'form': form}
    template = 'users/register.html'
    return render(request, template, context)
