from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Messanger
from .forms import MessageForm
from django.views.generic import UpdateView, DeleteView


class DeleteMessage(DeleteView):
    model = Messanger
    success_url = "/communication/"
    template_name = 'messanger/delete_message.html'

class UpdateMessage(UpdateView):
    model = Messanger
    template_name = 'messanger/update_post.html'
    form_class = MessageForm
    success_url = "/communication/"