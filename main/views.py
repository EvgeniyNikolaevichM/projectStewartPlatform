from django.shortcuts import render, redirect
from .models import matrix, stewart_platform, law_for_platform, law_for_system,stewart_platform_system
from django.http import HttpResponse
from django.db import transaction

import  logging


logger = logging.getLogger('TEST_LOGGER_NAME')


def index(request):
    # matrix = matrix.objects.all()
    # stewart_platform = stewart_platform.objects.all()
    # law_for_platform = law_for_platform.objects.all()
    # law_for_system = law_for_system.objects.all()
    # stewart_platform_system = stewart_platform_system.objects.all()
    logger.info("Загрузка страницы 'Главная'")
    return render(request, 'main/index.html')

def about(request):
    logger.info("Загрузка страницы 'О нас'")
    return render(request, 'main/about.html')

def admin(request):
    logger.info("Загрузка страницы 'Админ'")
    return redirect('admin')

def StewartPlatform(request):
    logger.info("Загрузка страницы 'Платформы'")
    return render(request, 'main/StewartPlatform.html')

# @transaction.atomic
def create(request):
    logger.info("Добавление в БД")
   #  error = ''
   #  if request.method == 'POST':
   #          form = TaskForm(request.POST)
   #          if form.is_valid():
   #              form.save()
   #              return redirect('home')
   #          else:
   #               error = 'форма была неверной'
   #  form = TaskForm()
   #  context={
   #          'form': form,
   #          'error': error
   # }
    return render(request, 'main/create.html')