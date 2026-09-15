from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from .models import Usuario
from .serializers import UsuarioSerializer

#APIS RESTFUL
#GET /USUARIOS
#POST /USUARIOS 

@api_view(["GET", "POST"])
def usuarios_list(request):
    #obtener usuarios
    if request.method == "GET":
        usuarios = Usuario.objects.all()
        #serializar - Objeto de Py --> JSON
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Usuario creado correctamente"}, status=status.HTTP_201_CREATED)
        return Response({"mensaje": "Error al crear el usuario"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def usuarios_detail (request, pk):
    if request.method == "GET":
        usuario = get_object_or_404(Usuario, pk=pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method == "PUT":
        usuario = get_object_or_404(Usuario, pk=pk)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Usuario actualizado correctamente"}, status=status.HTTP_200_OK)
        return Response({"mensaje": "Error al actualizar el usuario"}, status=status.HTTP_400_BAD_REQUEST)


    if request.method == "DELETE":
        usuario = get_object_or_404(Usuario, pk=pk)
        usuario.delete()
        return Response({"mensaje": "Usuario eliminado correctamente"}, status=status.HTTP_200_OK)

# --------------------------------------------------

@api_view(["GET", "POST"])
def actividades_list(request):
    #obtener actividad
    if request.method == "GET":
        actividades = Actividad.objects.all()
        #serializar - Objeto de Py --> JSON
        serializer = ActividadSerializer(actividades, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = ActividadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Actividad creada correctamente"}, status=status.HTTP_201_CREATED)
        return Response({"mensaje": "Error al crear la actividad"}, status=status.HTTP_400_BAD_REQUEST)