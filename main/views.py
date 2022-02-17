from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponse
from .forms import TaskForm

import  logging


logger = logging.getLogger('TEST_LOGGER_NAME')


def index(request):
    tasks = Task.objects.all()
    logger.info("Загрузка страницы 'Главная'")
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    logger.info("Загрузка страницы 'О нас'")
    return render(request, 'main/about.html')

def admin(request):
    logger.info("Загрузка страницы 'Админ'")
    return redirect('admin')

def StewartPlatform(request):
    logger.info("Загрузка страницы 'Платформы'")
    return render(request, 'main/StewartPlatform.html')

def create(request):
    logger.info("Добавление в БД")
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