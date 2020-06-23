from django.urls import path

from . import views


urlpatterns = [
    path('list/', views.project_list, name='project_list'),
    path('create/', views.project_create, name='project_create'),
]
