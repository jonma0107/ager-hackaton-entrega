from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from productosApp.serializers import ProductosSerializer
from .models import Productos
from rest_framework import status 
# Create your views here.

class ProductoViewsRegistrar(APIView):
    #Registrar Producto
    def post(self, request):
        serializer = ProductosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Producto creado exitosamente",status=status.HTTP_201_CREATED)

class ProductosViewsList(APIView):
    #lista de productos
    def get(self, request):
        ProductosModel = Productos.objects.all()
        serializer = ProductosSerializer(ProductosModel, many = True)
        return Response (serializer.data)

class ProductosViewsUpdate(APIView):
    #Editar un producto en específico
    def put (self, request, pk):
        ProductosModel = Productos.objects.get(pk=pk)
        serializer = ProductosSerializer(ProductosModel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error_messages)

class ProductosViewsDelete(APIView):
    #Borrar un producto en específico
    def delete (self, request, pk):
        ProductosModel = Productos.objects.get(pk=pk)
        ProductosModel.delete()
        return Response(status = status.HTTP_202_ACCEPTED)

class ProductosViewsBuscarId(APIView):
    #Buscar Productos por id
	def get(self, request, pk):
		productos = Productos.objects.filter(id=pk)
		serializer = ProductosSerializer(productos,many=True)
		return Response(serializer.data)


# metodos de filtrado especiales

class ProductosViewsBuscarNombre(APIView):
    #Filtrar Productos por nombre
	def get(self, request, nombre):
		productos = Productos.objects.filter(nombre__contains=nombre)
		serializer = ProductosSerializer(productos,many=True)
		return Response(serializer.data)

class ProductosViewsBuscarPrecio(APIView):
    #Filtrar Productos por precioLibra
	def get(self, request, precioLibra):
		productos = Productos.objects.filter(precioLibra__contains=precioLibra)
		serializer = ProductosSerializer(productos,many=True)
		return Response(serializer.data)

class ProductosViewsBuscarCosecha(APIView):
    #Filtrar Productos por cosecha
	def get(self, request, cosecha):
		productos = Productos.objects.filter(cosecha__contains=cosecha)
		serializer = ProductosSerializer(productos,many=True)
		return Response(serializer.data)

class ProductosViewsBuscarCategoria(APIView):
    #Filtrar Productos por categoria
	def get(self, request, categoria):
		productos = Productos.objects.filter(categoria__contains=categoria)
		serializer = ProductosSerializer(productos,many=True)
		return Response(serializer.data)

class ProductosViewsBuscarFase(APIView):
    #Filtrar Productos por fase
	def get(self, request, fase):
		productos = Productos.objects.filter(fase__contains=fase)
		serializer = ProductosSerializer(productos,many=True)
		return Response(serializer.data)

class ProductosViewsBuscarEstado(APIView):
    #Filtrar Productos por estado
	def get(self, request, estado):
		productos = Productos.objects.filter(estado__contains=estado)
		serializer = ProductosSerializer(productos,many=True)
		return Response(serializer.data)