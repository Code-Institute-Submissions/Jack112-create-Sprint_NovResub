from django.shortcuts import render
from .models import Project

# Create your views here.

def projects(request):

    projects = Project.objects.all()
    context = {
        'projects': projects,
    }

    return render(request, 'projects/projects.html', context)


def project(request, project_id):

    context = {}
    return render(request, 'projects/project.html', context)