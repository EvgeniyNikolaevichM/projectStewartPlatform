#функционально-ориентированный подход:

from django.shortcuts import render, redirect
from .models import *
from django.db import transaction
# from .forms import Create_sytemForm
#
# import logging
# logger = logging.getLogger('TEST_LOGGER_NAME')
#
#
# @transaction.atomic
# def create_system(request):
#     logger.info("Добавление системы")
#     error = ''
#     if request.method == 'POST':
#             form = Create_sytemForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('home')
#             else:
#                  error = 'форма была неверной'
#     form = Create_sytemForm()
#     context={
#             'form': form,
#             'error': error
#    }
#     return render(request, 'systemStewartPlatform/create_system.html', context)
#
#
# def read_system(request):
#     system = system_stewart_platform.objects.all()
#     logger.info("Просмотр систем")
#     return render(request, 'systemStewartPlatform/read_system.html', {'system': system})


#Классовый подход:

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class systemListView(ListView):
    model = system_stewart_platform
    template_name = "systemStewartPlatform/system/systemListView.html"

class systemDetailView(DetailView):
    model = system_stewart_platform
    template_name = "systemStewartPlatform/system/systemDetailView.html"

class systemCreateView(CreateView):
    model = system_stewart_platform
    template_name = 'systemStewartPlatform/system/systemCreateView.html'
    fields = ['title', 'discription_system', 'law_system', 'x_max_matrix', 'y_max_matrix']

class systemEditView(UpdateView):
    model = system_stewart_platform
    template_name = 'systemStewartPlatform/system/systemEditView.html'
    fields = ['title', 'discription_system', 'law_system', 'x_max_matrix', 'y_max_matrix']

class systemDeleteView(DeleteView):
    model = system_stewart_platform
    template_name = 'systemStewartPlatform/system/systemDeleteView.html'
    success_url = reverse_lazy('home')


class platformListView(ListView):
    model = stewart_platform
    template_name = "systemStewartPlatform/platform/platformListView.html"

class platformDetailView(DetailView):
    model = stewart_platform
    template_name = "systemStewartPlatform/platform/platformDetailView.html"

class platformCreateView(CreateView):
    model = stewart_platform
    template_name = 'systemStewartPlatform/platform/platformCreateView.html'
    fields = ['system_stewart_platform', 'title', 'discription', 'ip_adress', 'port', 'position_x_in_matrix',
              'position_y_in_matrix']

class platformEditView(UpdateView):
    model = stewart_platform
    template_name = 'systemStewartPlatform/platform/platformEditView.html'
    fields = ['system_stewart_platform', 'title', 'discription', 'ip_adress', 'port', 'position_x_in_matrix',
              'position_y_in_matrix']

class platformDeleteView(DeleteView):
    model = stewart_platform
    template_name = 'systemStewartPlatform/platform/platformDeleteView.html'
    success_url = reverse_lazy('home')


class LawWaveListView(ListView):
    model = law_for_platform_wave
    template_name = "systemStewartPlatform/law_wave/LawWaveListView.html"

class LawWaveDetailView(DetailView):
    model = law_for_platform_wave
    template_name = "systemStewartPlatform/law_wave/LawWaveDetailView.html"

class LawWaveCreateView(CreateView):
    model = law_for_platform_wave
    template_name = 'systemStewartPlatform/law_wave/LawWaveCreateView.html'
    fields = ['stewart_platform', 'time', 'x_coordinate', 'y_coordinate', 'z_coordinate', 'γ_roll_x',
              'θ_pitch_y', 'ψ_yaw_z']

class LawWaveEditView(UpdateView):
    model = law_for_platform_wave
    template_name = 'systemStewartPlatform/law_wave/LawWaveEditView.html'
    fields = ['stewart_platform', 'time', 'x_coordinate', 'y_coordinate', 'z_coordinate', 'γ_roll_x',
              'θ_pitch_y', 'ψ_yaw_z']

class LawWaveDeleteView(DeleteView):
    model = law_for_platform_wave
    template_name = 'systemStewartPlatform/law_wave/LawWaveDeleteView.html'
    success_url = reverse_lazy('home')


class LawVibrationsListView(ListView):
    model = law_for_platform_vibrations
    template_name = "systemStewartPlatform/law_Vibrations/LawVibrationsListView.html"

class LawVibrationsDetailView(DetailView):
    model = law_for_platform_vibrations
    template_name = "systemStewartPlatform/law_Vibrations/LawVibrationsDetailView.html"

class LawVibrationsCreateView(CreateView):
    model = law_for_platform_vibrations
    template_name = 'systemStewartPlatform/law_Vibrations/LawVibrationsCreateView.html'
    fields = ['stewart_platform', 'time', 'x_coordinate', 'y_coordinate', 'z_coordinate', 'γ_roll_x',
              'θ_pitch_y', 'ψ_yaw_z']

class LawVibrationsEditView(UpdateView):
    model = law_for_platform_vibrations
    template_name = 'systemStewartPlatform/law_Vibrations/LawVibrationsEditView.html'
    fields = ['stewart_platform', 'time', 'x_coordinate', 'y_coordinate', 'z_coordinate', 'γ_roll_x',
              'θ_pitch_y', 'ψ_yaw_z']

class LawVibrationsDeleteView(DeleteView):
    model = law_for_platform_vibrations
    template_name = 'systemStewartPlatform/law_Vibrations/LawVibrationsDeleteView.html'
    success_url = reverse_lazy('home')