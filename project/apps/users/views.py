from django.shortcuts import render


def login(request):
    template_name = 'users/login.html'
    return render(request, template_name)
