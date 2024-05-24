from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Messanger
from .forms import MessageForm
from django.views.generic import ListView