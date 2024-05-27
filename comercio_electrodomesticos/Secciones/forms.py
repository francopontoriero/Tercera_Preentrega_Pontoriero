from django import forms
from . import models


class Productos_categoriaForm(forms.ModelForm):
    class Meta:
        model = models.Productos_categoria
        fields = "__all__"

