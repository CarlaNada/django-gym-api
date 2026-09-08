from django.db import models

# Create your models here.

class Usuario(models.Model):
    #cambiar por el user de django
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_alta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Turno(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField()
    asistencia = models.BooleanField(default=False)

    def __str__(self):
        return f"Turno {self.nombre} - {self.fecha_hora}"