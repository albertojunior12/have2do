from django.urls import path

from . import views


urlpatterns = [
    path('list/', views.project_list, name='project_list'),
    path('create/', views.project_create, name='project_create'),
    path('update/<int:id>/', views.project_update, name='project_update'),
    path('detail/<int:id>/', views.project_detail, name='project_detail'),
]
