from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

@login_required(login_url='/users/login_form/')
def create_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            form.save()
            return redirect('main:task_board')
        else:
            error = 'error'
    form = TaskForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'tasks/create_task.html', data)

class ReadTask(DetailView):
    model = Task
    template_name = 'tasks/read_task.html'
    context_object_name = 'task'

class UpdateTask(UpdateView):
    model = Task
    template_name = 'tasks/update_task.html'
    form_class = TaskForm

class DeleteTask(DeleteView):
    model = Task
    success_url = '/task_board/'
    template_name = 'tasks/delete_task.html'