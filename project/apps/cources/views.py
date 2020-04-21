from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template_name = "bootstrap4/index.html"
    return render(request, template_name)
