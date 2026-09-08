from rest_framework import serializers
from .models import Usuario, Turno

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            #"id",
            "nombre",
            "apellido",
            "dni",
            "email",
            "fecha_nacimiento",
            "activo",
            #"fecha_alta"
        ]
        #'__all__' # Expone todos los campos del modelo (nombre, dni, etc.)
        read_only_fields = ["id", 'fecha_alta'] # Campo de solo lectura

class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ["__all__"]
        read_only_fields = ["id"]