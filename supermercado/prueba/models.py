from django.db import models

class Lista(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marcado = models.BooleanField(default=False)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre
