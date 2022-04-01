from django.shortcuts import render, redirect
from .models import system_stewart_platform
from django.db import transaction
from .forms import Create_sytemForm

import logging
logger = logging.getLogger('TEST_LOGGER_NAME')


@transaction.atomic
def create_system(request):
    logger.info("Добавление системы")
    error = ''
    if request.method == 'POST':
            form = Create_sytemForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                 error = 'форма была неверной'
    form = Create_sytemForm()
    context={
            'form': form,
            'error': error
   }
    return render(request, 'systemStewartPlatform/create_system.html', context)


def read_system(request):
    system = system_stewart_platform.objects.all()
    logger.info("Просмотр систем")
    return render(request, 'systemStewartPlatform/read_system.html', {'system': system})