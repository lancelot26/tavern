from django.shortcuts import render
from tasks.models import Task
from django.views.generic import DetailView, ListView
from django.db.models import Q

def tavern(request):
    return render(request, 'main/tavern.html')

def task_board(request):
    tasks = Task.objects.order_by('-date')
    return render(request, 'main/task_board.html', {'tasks':tasks})

def my_task_board(request):
    tasks = Task.objects.filter(author=request.user).order_by('-date')
    return render(request, 'main/my_task_board.html', {'tasks':tasks})

def communication(request):
    return render(request, 'main/communication.html')

def food_n_bar(request):
    return render(request, 'main/food_n_bar.html')

def inn(request):
    return render(request, 'main/inn.html')

class TaskBoardFilter(ListView):
    model = Task
    template_name = 'main/task_board_filter.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Task.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(reward__icontains=query)
        )
        return object_list