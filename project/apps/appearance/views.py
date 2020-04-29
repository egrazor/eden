from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404


def index(request):
    template_name = 'appearance/index.html'
    return render(request, template_name)
