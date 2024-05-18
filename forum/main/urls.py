from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.tavern, name='tavern'),
    path('task_board/', views.task_board, name='task_board'),
    path('guild_task_board/', views.guild_task_board, name='guild_task_board'),
    path('communication/', views.communication, name='communication'),
    path('food_n_bar/', views.food_n_bar, name='food_n_bar'),
    path('inn/', views.inn, name='inn'),
]