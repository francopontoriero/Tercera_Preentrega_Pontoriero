from django.shortcuts import render, redirect
from . import models   
from Secciones.forms import Productos_categoriaForm

def index(request):
    consulta = models.Productos_categoria.objects.all()
    contexto = {"Producto_categoria" : consulta}
    return render(request, "Secciones/index.html", contexto)

def productocategoria_create(request):
    if request.method == "POST":
        form = Productos_categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Secciones:index")

    else:
        form = Productos_categoriaForm()
    return render(request, "Secciones/index_form.html", {"form": form})

