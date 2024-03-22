# En tu archivo models.py

from django.db import models
from django.utils import timezone

class Facultad(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=100)
    ubicacion = models.URLField(blank=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)


    def __str__(self):
        return self.nombre

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    semestres = models.IntegerField()
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    recorrido = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.nombre

class Bloque(models.Model):
    codigo_identificativo= models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)  # Campo booleano para el estado, por defecto True (activo)
    imagen = models.ImageField(upload_to='media/bloque_fotos/')  # Directorio donde se guardarán las imágenes
    link = models.URLField(blank=True)  # Campo para el enlace, puede estar vacío

    def __str__(self):
        return self.nombre


