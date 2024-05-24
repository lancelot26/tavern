from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Messanger
from .forms import MessageForm
from django.shortcuts import get_object_or_404

@login_required(login_url='/users/login_form/')
def message_create(request):
    error = ''
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            newmessage = form.save(commit=False)
            newmessage.author = request.user
            newmessage.save()
            form.save()
            return redirect('main:communication')
        else:
            error = 'Incorrect data entered'
    form = MessageForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'messanger/message_create.html', data)