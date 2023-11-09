from django.db import models

# Create your models here.
class Talleres(models.Model):
    nombre = models.CharField(max_length=64)
    generacion = models.IntegerField()

class Prospecto(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)

class Inscrito(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    objetivo = models.TextField(blank=True)