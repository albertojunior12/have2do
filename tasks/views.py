from django.shortcuts import render, redirect

from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/task_list.html', context)


def task_create(request):
    if request.method == 'POST':
        title_data = request.POST['title']
        description_data = request.POST['description']
        Task.objects.create(
            title=title_data,
            description=description_data,
        )
        return redirect('/tasks/')
    return render(request, 'tasks/task_create.html')


def task_detail(request, id):
    task = Task.objects.get(id=id)
    context = {
        'task': task
    }
    return render(request, 'tasks/task_detail.html', context)


def task_update(request, id):
    task = Task.objects.get(id=id)
    context = {'task': task}
    if request.method == 'POST':
        new_title = request.POST['title']
        new_description = request.POST['description']

        task.title = new_title
        task.description = new_description
        task.save()
        return redirect('/tasks/')
    return render(request, 'tasks/task_update.html', context)


def task_delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/tasks/')
