from django.shortcuts import redirect, render
from django.contrib import admin
from django.urls import path, include


def redirect_to_tasks(request):
    return render(request, 'index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_tasks),
    path('tasks/', include('tasks.urls')),
    path('projects/', include('projects.urls')),
]
