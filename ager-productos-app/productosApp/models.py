from django.db import models

# Create your models here.

class Productos (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre", max_length=30)
    precioLibra = models.CharField(max_length=30)
    cosecha = models.DateField()
    categoria = models.CharField("Categoria", max_length=50)
    fase = models.DateField("Fase", max_length=50,null=True)
    estado = models.CharField("Estado", max_length=50)