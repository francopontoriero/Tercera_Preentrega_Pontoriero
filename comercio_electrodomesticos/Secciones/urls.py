from django.contrib import admin
from django.urls import path
from . import views

app_name = "Secciones"

urlpatterns = [
    path("", views.index, name="index"),
    path("productocategoria/create", views.productocategoria_create, name="form")
]

