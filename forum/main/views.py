from django.shortcuts import render
from tasks.models import Task

def tavern(request):
    return render(request, 'main/tavern.html')

def task_board(request):
    tasks = Task.objects.order_by('-date')
    return render(request, 'main/task_board.html', {'tasks':tasks})

def guild_task_board(request):
    return render(request, 'main/guild_task_board.html')

def communication(request):
    return render(request, 'main/communication.html')

def food_n_bar(request):
    return render(request, 'main/food_n_bar.html')

def inn(request):
    return render(request, 'main/inn.html')