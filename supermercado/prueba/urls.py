# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_supermercado, name='lista_supermercado'),
    path('toggle/<int:producto_id>/', views.toggle_producto, name='toggle_producto'),
]
