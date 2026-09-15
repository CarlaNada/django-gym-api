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

"""    
class Turno(models.Model):
    ESTADOS = [
        ('RESERVADO', 'Reservado'),
        ('ASISTIO', 'Asistió'),
        ('CANCELADO', 'Cancelado'),
    ]

    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, related_name='turnos')
    fecha = models.DateField()                  # Ej: 2026-10-15
    hora_inicio = models.TimeField()            # Ej: 08:00:00
    hora_fin = models.TimeField()               # Ej: 09:00:00
    estado = models.CharField(max_length=20, choices=ESTADOS, default='RESERVADO')
"""