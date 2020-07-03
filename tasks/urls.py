from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('detail/<int:id>/', views.task_detail, name='task_detail'),
    path('update/<int:id>/', views.task_update, name='task_update'),
    path('delete/<int:id>/', views.task_delete, name='task_delete'),
    path('done/<int:id>/', views.task_done, name='task_done'),
    path('cancel/<int:id>/', views.task_cancel, name='task_cancel'),
]
