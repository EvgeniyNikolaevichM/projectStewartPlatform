from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponse
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def admin(request):
    return redirect('admin')

def StewartPlatform(request):
    return render(request, 'main/StewartPlatform.html')

def create(request):
    error = ''
    if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                 error = 'форма была неверной'
    form = TaskForm()
    context={
            'form': form,
            'error': error
   }
    return render(request, 'main/create.html', context)