from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from tasks.models import Task
from messanger.models import Messanger
from messanger.forms import MessageForm
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

@login_required(login_url='/users/login_form/')
def communication(request):
    error =''
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            newmessage = form.save(commit=False)
            newmessage.author = request.user
            newmessage.save()
            form.save()
            return redirect('main:communication')
        else:
            error = 'error'
    form = MessageForm()
    messages = Messanger.objects.order_by('-date')
    data = {
        'form':form,
        'messages':messages,
        'error':error
    }
    return render(request, 'main/communication.html', data)

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