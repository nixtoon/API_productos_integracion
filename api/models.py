from django.db import models

# Create your models here.

class Marca(models.Model):
  nombre = models.CharField(max_length=30)

  def __str__(self):
    return self.nombre
  

class Producto(models.Model):
  nombre = models.CharField(max_length=50)
  precio = models.IntegerField(max_length=8)
  marca = models.ForeignKey(Marca, on_delete = models.PROTECT)

  def __str__(self):
    return self.nombre

