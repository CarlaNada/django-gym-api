from django.contrib import admin
from django.urls import path
from .views import usuarios_list, usuarios_detail

urlpatterns = [
    path('', usuarios_list, name='usuarios-list'),
    path('<int:pk>/', usuarios_detail, name='usuarios_detail_api')
]
