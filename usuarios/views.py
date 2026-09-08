from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from .models import Usuario, Turno
from .serializers import UsuarioSerializer, TurnoSerializer

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
def turno(request):
    #obtener turno
    if request.method == "GET":
        turnos = Turno.objects.all()
        #serializar - Objeto de Py --> JSON
        serializer = TurnoSerializer(turnos, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = TurnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Turno creado correctamente"}, status=status.HTTP_201_CREATED)
        return Response({"mensaje": "Error al crear el turno"}, status=status.HTTP_400_BAD_REQUEST)