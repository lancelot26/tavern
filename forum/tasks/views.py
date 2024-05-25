from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Task, Comment
from .forms import TaskForm, CommentForm, UpdateTaskForm
from django.shortcuts import get_object_or_404

@login_required(login_url='/users/login_form/')
def create_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.author_name = str(newpost.author)
            newpost.save()
            form.save()
            return redirect('main:my_task_board')
        else:
            error = 'error'
    form = TaskForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'tasks/create_task.html', data)

@login_required(login_url='login')
def add_comment_p(request, comment_id):
    form = CommentForm()
    task = get_object_or_404(Task, id=comment_id)
    author = request.user
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = author
            comment.task = task
            comment.save()
            return redirect('tasks:read_task_public', task.id)
    return render(request, 'tasks/comment.html', {'form': form})


@login_required(login_url='login')
def add_comment(request, comment_id):
    form = CommentForm()
    task = get_object_or_404(Task, id=comment_id)
    author = request.user
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = author
            comment.task = task
            comment.save()
            return redirect('tasks:read_task', task.id)
    return render(request, 'tasks/comment.html', {'form': form})

class ReadTask(DetailView):
    model = Task
    template_name = 'tasks/read_task.html'
    context_object_name = 'task'

class ReadTaskPublic(DetailView):
    model = Task
    template_name = 'tasks/read_task_public.html'
    context_object_name = 'task'

class UpdateTask(UpdateView):
    model = Task
    template_name = 'tasks/update_task.html'
    form_class = UpdateTaskForm

    def get_initial(self):
        return {'updated_task':'(updated)'}

class DeleteTask(DeleteView):
    model = Task
    success_url = '/my_task_board/'
    template_name = 'tasks/delete_task.html'