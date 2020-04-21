from django.shortcuts import render


def index(request):
    template_name = 'fullcalendar/fullcalendar.html'
    return render(request, template_name)
