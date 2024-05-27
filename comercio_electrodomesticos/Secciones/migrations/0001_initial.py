# Generated by Django 5.0.4 on 2024-05-13 06:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Identificador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_de_barras', models.PositiveBigIntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Identificador',
                'verbose_name_plural': 'Identificadores',
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Productos_categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.PositiveBigIntegerField()),
                ('categoria', models.CharField(choices=[('cocina', 'Productos de Cocina'), ('cuidado_personal', 'Productos de Cuidado Personal'), ('entretenimiento', 'Productos de Entretenimiento'), ('pequenos', 'Productos Pequeños')], max_length=20)),
                ('codigo_de_barras', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Secciones.identificador')),
                ('nombre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Secciones.productos')),
            ],
            options={
                'verbose_name': 'Producto_categoria',
                'verbose_name_plural': 'Productos_categoria',
            },
        ),
    ]