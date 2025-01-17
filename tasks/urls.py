from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListAPIView.as_view(), name='task-list'),
    path('create/', views.TaskCreateAPIView.as_view(), name='task-create'), 
    path('delete/<int:task_id>/', views.TaskDeleteAPIView.as_view(), name='task-delete'),
]
