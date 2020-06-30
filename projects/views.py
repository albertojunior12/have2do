from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Project
from tasks.models import Task
from .forms import ProjectForm


def project_list(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/project_list.html', context)


def project_create(request):
    form = ProjectForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('project_list'))
        else:
            return render(request, 'projects/project_create.html', context)
    return render(request, 'projects/project_create.html', context)


def project_update(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(request.POST or None, instance=project)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('project_detail', kwargs={'id': id}))
        else:
            return render(request, 'projects/project_update.html', context)
    return render(request, 'projects/project_update.html', context)


def project_detail(request, id):
    project = Project.objects.get(id=id)
    context = {'project': project}
    return render(request, 'projects/project_detail.html', context)
