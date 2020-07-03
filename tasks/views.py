from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/task_list.html', context)


def task_create(request):
    form = TaskForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('task_list'))
    return render(request, 'tasks/task_create.html', context)


def task_detail(request, id):
    task = Task.objects.get(id=id)
    context = {
        'task': task
    }
    return render(request, 'tasks/task_detail.html', context)


def task_update(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('task_list'))
    return render(request, 'tasks/task_update.html', context)


def task_delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect(reverse_lazy('task_list'))


def task_done(request, id):
    task = Task.objects.get(id=id)
    task.status = Task.DONE
    task.save()
    return redirect(reverse_lazy('project_detail', kwargs={'id': task.project.id}))


def task_cancel(request, id):
    task = Task.objects.get(id=id)
    task.status = Task.CANCELED
    task.save()
    return redirect(reverse_lazy('project_detail', kwargs={'id': task.project.id}))