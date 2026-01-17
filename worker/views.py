import random
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, WorkerRegistrationForm, WorkerLoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Worker
from django.contrib.auth.decorators import login_required

#Create your views here.

@login_required
def edit_worker(request):
    worker = get_object_or_404(Worker, user = request.user)
    if request.method == 'POST':
        form = WorkerRegistrationForm(request.POST, request.FILES, instance=worker)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = WorkerRegistrationForm(instance=worker)
    return render(request, 'registeration/edit_worker.html', {'form': form})

@login_required
def register_form(request):
    if request.method == 'POST':
        form = WorkerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            worker = form.save(commit=False)
            worker.user = request.user
            worker.save()
            return redirect('dashboard')
    else:
        form = WorkerRegistrationForm()
    return render(request, 'registeration/register_form_w.html', {'form': form})

@login_required
def dashboard(request):
    worker = get_object_or_404(Worker, user=request.user)
    return render(request, 'dashboard.html', {'worker': worker})

@login_required
def logout_view(request):
    logout(request)
    return redirect('register')

def login_view(request):
    if request.method == 'POST':
        form = WorkerLoginForm(request,  data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = WorkerLoginForm()
    return render(request, 'registeration/login.html', {'form': form})
            

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('register_form')
    else:
        form = UserRegistrationForm()
    return render(request, 'registeration/register.html', {'form': form})