from django.urls import path

from .views import *


urlpatterns = [
    # path('create_system', views.create_system, name='create_system'),
    # path('read_system', views.read_system, name='read_system'),
    path('systemListView', systemListView.as_view(), name='systemListView'),
    path('systemDetailView/<int:pk>/', systemDetailView.as_view(), name='systemDetailView'),
    path('systemNewView', systemCreateView.as_view(), name='systemCreateView'),
    path('systemDetailView/<int:pk>/edit/', systemEditView.as_view(), name='systemEditView'),
    path('systemDeleteView/<int:pk>/delete/', systemDeleteView.as_view(), name='systemDeleteView'),

    path('platformListView', platformListView.as_view(), name='platformListView'),
    path('platformDetailView/<int:pk>/', platformDetailView.as_view(), name='platformDetailView'),
    path('platformNewView', platformCreateView.as_view(), name='platformCreateView'),
    path('platformDetailView/<int:pk>/edit/', platformEditView.as_view(), name='platformEditView'),
    path('platformDeleteView/<int:pk>/delete/', platformDeleteView.as_view(), name='platformDeleteView'),

    path('LawWaveListView', LawWaveListView.as_view(), name='LawWaveListView'),
    path('LawWaveDetailView/<int:pk>/', LawWaveDetailView.as_view(), name='LawWaveDetailView'),
    path('LawWaveNewView', LawWaveCreateView.as_view(), name='LawWaveCreateView'),
    path('LawWaveDetailView/<int:pk>/edit/', LawWaveEditView.as_view(), name='LawWaveEditView'),
    path('LawWaveDeleteView/<int:pk>/delete/', LawWaveDeleteView.as_view(), name='LawWaveDeleteView'),

    path('LawVibrationsListView', LawVibrationsListView.as_view(), name='LawVibrationsListView'),
    path('LawVibrationsDetailView/<int:pk>/', LawVibrationsDetailView.as_view(), name='LawVibrationsDetailView'),
    path('LawVibrationsNewView', LawVibrationsCreateView.as_view(), name='LawVibrationsCreateView'),
    path('LawVibrationsDetailView/<int:pk>/edit/', LawVibrationsEditView.as_view(), name='LawVibrationsEditView'),
    path('LawVibrationsDeleteView/<int:pk>/delete/', LawVibrationsDeleteView.as_view(), name='LawVibrationsDeleteView'),
]