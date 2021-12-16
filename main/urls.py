from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('StewartPlatform', views.StewartPlatform, name='StewartPlatform'),
    path('create', views.create, name='create'),
    path('admin/', views.admin, name='admin'),
]
