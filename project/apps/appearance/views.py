from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from cources.models import Faculty, Department, Direction
from users.models import EdenUser


def index(request):
    faculties = Faculty.objects.all()
    departments = Department.objects.all()
    directions = Direction.objects.all()
    context = {
        'faculties':  faculties,
        'departments': departments,
        'directions': directions
    }
    template_name = 'appearance/index.html'
    return render(request, template_name, context)


def personal(request):
    template_name = 'appearance/personal_page.html'

    if request.user.is_authenticated:
        user = request.user
    else:
        raise Http404

    context = {
        'user': user,
    }
    return render(request, template_name, context)

