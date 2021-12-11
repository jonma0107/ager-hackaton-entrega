from django.db.models import fields
from rest_framework import serializers
from .models import Productos

#creacion del serializador para el modelo hecho

class ProductosSerializer(serializers.ModelSerializer):
    
#Se serializan todos los campos

    class Meta:
        model = Productos
        fields = '__all__'