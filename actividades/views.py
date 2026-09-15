from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from .models import Actividad
from .serializers import ActividadSerializer

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
