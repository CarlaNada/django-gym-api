from django.contrib import admin
from django.urls import path
from .views import actividades_list

urlpatterns = [
    path('api/actividades/', actividades_list, name='actividad-list')
]
