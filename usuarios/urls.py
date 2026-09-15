from django.contrib import admin
from django.urls import path
from .views import usuarios_list, usuarios_detail

urlpatterns = [
    path('api/usuarios/', usuarios_list, name='usuarios-list'),
    path('api/usuarios/<int:pk>/', usuarios_detail, name='usuarios_detail_api')
]
