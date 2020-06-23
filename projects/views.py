from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Project


def project_list(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/project_list.html', context)


def project_create(request):
    if request.method == 'POST':
        name_data = request.POST['name']
        description_data = request.POST['description']
        color_data = request.POST['color']
        Project.objects.create(
            name=name_data,
            description=description_data,
            color=color_data
        )
        return redirect(reverse_lazy('project_list'))
    return render(request, 'projects/project_create.html')
