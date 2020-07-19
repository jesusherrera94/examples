from django.db import models

# Create your models here.
#crear una clase por cada tabla que se quiera crear en la BD

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=7)

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()
    
class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entegrado = models.BooleanField()