from django import forms
from .models import Lista, Producto

class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ['nombre']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio','marcado', 'lista']
