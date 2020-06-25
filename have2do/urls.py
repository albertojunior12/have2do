from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import admin
from django.urls import path, include


def redirect_to_home(request):
    return redirect(reverse_lazy('project_list'))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_home),
    path('categories/', include('categories.urls')),
    path('projects/', include('projects.urls')),
    path('tasks/', include('tasks.urls')),
]
