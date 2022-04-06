#функционально-ориентированный подход:

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


#Классовый подход:

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class systemListView(ListView):
    model = system_stewart_platform
    template_name = "systemStewartPlatform/systemListView.html"

class systemDetailView(DetailView):
    model = system_stewart_platform
    template_name = "systemStewartPlatform/systemDetailView.html"

class systemCreateView(CreateView):
    model = system_stewart_platform
    template_name = 'systemStewartPlatform/systemCreateView.html'
    fields = ['title', 'discription_system', 'law_system', 'x_max_matrix', 'y_max_matrix']

class systemEditView(UpdateView):
    model = system_stewart_platform
    template_name = 'systemStewartPlatform/systemEditView.html'
    fields = ['title', 'discription_system', 'law_system', 'x_max_matrix', 'y_max_matrix']

class systemDeleteView(DeleteView):
    model = system_stewart_platform
    template_name = 'systemStewartPlatform/systemDeleteView.html'
    success_url = reverse_lazy('home')
