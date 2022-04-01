from django.urls import path
from .import views

urlpatterns = [
    path('create_system', views.create_system, name='create_system'),
    path('read_system', views.read_system, name='read_system'),
]
