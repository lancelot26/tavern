from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def reg_form(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('main:tavern')
    else:
        form = UserCreationForm()
    return render(request, 'users/reg_form.html', {'form':form})

def login_form(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('main:tavern')
    else:
        form = AuthenticationForm()
        return render(request, 'users/login_form.html', {'form':form})

def logout_form(request):
    if request.method =='POST':
        logout(request)
        return redirect('main:tavern')
