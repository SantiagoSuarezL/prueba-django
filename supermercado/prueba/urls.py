from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_supermercado, name='lista_supermercado'),
]
