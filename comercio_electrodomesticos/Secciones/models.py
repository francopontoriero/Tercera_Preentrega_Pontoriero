from django.db import models


class Productos(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.nombre.capitalize()}"
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
       
class Identificador(models.Model):
    codigo_de_barras = models.PositiveBigIntegerField(unique=True)

    def __str__(self):
        return f"{self.codigo_de_barras}"
    
    class Meta:
        verbose_name = "Identificador"
        verbose_name_plural = "Identificadores"

class Productos_categoria(models.Model):
    categorias = (
        ('Producto de Cocina', 'Producto de Cocina'),
        ('Producto de Cuidado Personal', 'Producto de Cuidado Personal'),
        ('Producto de Entretenimiento', 'Producto de Entretenimiento'),
        ('Producto Pequeño', 'Producto Pequeño'),
    )
    nombre = models.ForeignKey(Productos, on_delete=models.SET_NULL, null=True, blank=True)
    precio = models.PositiveBigIntegerField()
    categoria = models.CharField(max_length=100, choices=categorias)
    codigo_de_barras = models.ForeignKey(Identificador, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.codigo_de_barras}) {self.nombre} : $ {self.precio} ({self.categoria})"
    
    class Meta:
        verbose_name = "Producto_categoria"
        verbose_name_plural = "Productos_categoria"