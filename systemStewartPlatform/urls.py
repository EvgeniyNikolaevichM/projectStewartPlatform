from django.urls import path
from .import views

from .views import systemListView, systemDetailView, systemCreateView, systemEditView, systemDeleteView


urlpatterns = [
    path('create_system', views.create_system, name='create_system'),
    path('read_system', views.read_system, name='read_system'),
    path('systemListView', systemListView.as_view(), name='systemListView'),
    path('systemDetailView/<int:pk>/', systemDetailView.as_view(), name='systemDetailView'),
    path('systemNewView', systemCreateView.as_view(), name='systemCreateView'),
    path('systemDetailView/<int:pk>/edit/', systemEditView.as_view(), name='systemEditView'),
    path('systemDeleteView/<int:pk>/delete/', systemDeleteView.as_view(), name='systemDeleteView'),
]
