from django.shortcuts import render
from .models import Project
from django.shortcuts import get_object_or_404
from .forms import ProjectForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def projects(request):
    """
    A view to render a list of projects
    """

    projects = Project.objects.all()
    context = {
        'projects': projects,
    }

    return render(request, 'projects/projects.html', context)


def project(request, project_id):
    """
    A view to render a single project
    """

    project = get_object_or_404(Project, pk=project_id)
    context = {
        'project': project
    }
    return render(request, 'projects/project.html', context)


@login_required
def add_project(request):
    """
    A view to add a new project
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('projects')

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project successfully added')
            return (redirect('projects'))
        else:
            messages.error(
                request,
                '''Unable to add a new project at this time.
                Please try again later''')

    else:
        form = ProjectForm()

    context = {
        'form': form,
    }

    return render(request, 'projects/add_project.html', context)


@login_required
def edit_project(request, project_id):
    """
    A view to render edit project form
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('projects')

    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project was successfully updated')
            return redirect('projects')
        else:
            messages.error(
                request,
                """Unable to update the project at this time.
                Please try again later""")
    else:
        form = ProjectForm(instance=project)
        messages.info(
            request,
            f'You are editing the following project: {project.name}')

    context = {
        'project': project,
        'form': form,
    }

    return render(request, 'projects/edit_project.html', context)


@login_required
def delete_project(request, project_id):
    """ view to delete a project """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(('projects'))

    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    messages.success(request, 'Successfully deleted a project!')
    return redirect(('projects'))
