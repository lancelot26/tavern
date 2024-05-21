from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('create/', views.create_task, name='create_task'),
    path('<int:pk>', views.ReadTask.as_view(), name='read_task'),
    path('<int:pk>p', views.ReadTaskPublic.as_view(), name='read_task_public'),
    path('<int:pk>/update/', views.UpdateTask.as_view(), name='update_task'),
    path('<int:pk>/delete/', views.DeleteTask.as_view(), name='delete_task'),
]