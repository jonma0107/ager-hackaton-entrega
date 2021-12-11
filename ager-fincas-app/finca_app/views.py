from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Finca
from .serializers import FincaSerializer

# Create your views here.

class FincaListado(APIView):
	"""
		View del listado de todas las Fincas
		
	"""
	def get(self, request):
		nombre_finca = Finca.objects.all()
		serializer = FincaSerializer(nombre_finca,many=True)
		return Response(serializer.data)
		


class FincaBuscarPorId(APIView):
	"""
		View de la Finca buscada por Id
		
	"""		
	def get(self, request, pk):
		nombre_finca = Finca.objects.filter(id=pk)
		serializer = FincaSerializer(nombre_finca,many=True)
		return Response(serializer.data)



class FincaRegistrar(APIView):
	"""
		View para Registrar la Finca
		
	"""
	def post(self, request):
		nombre_finca = Finca.objects.all()
		serializer = FincaSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)	
		else:
			return Response(serializer.error)



class FincaEditar(APIView):
	"""
		View para Editar la Finca
		
	"""
	def put(self, request, pk):
		nombre_finca = Finca.objects.get(pk=pk)
		serializer = FincaSerializer(nombre_finca,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
		 	return Response(serializer.error)
		 	

	
class FincaEliminar(APIView):
	"""
		View para Eliminar la Finca
		
	"""
	def delete(self, request, pk):
		id_usuario_finca = Finca.objects.get(pk=pk)
		id_usuario_finca.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class BuscarFincaPorNombreFinca(APIView):
	def get(self, request, nombre_finca):
		fincas = Finca.objects.filter(nombre_finca__contains=nombre_finca)
		serializer = FincaSerializer(fincas, many=True)
		return Response(serializer.data)

class BuscarFincaPorPropietario(APIView):
	def get(self, request, propietario):
		fincas = Finca.objects.filter(propietario__contains=propietario)
		serializer = FincaSerializer(fincas, many=True)
		return Response(serializer.data)

class BuscarFincaPorDepartamento(APIView):
	def get(self, request, departamento):
		fincas = Finca.objects.filter(departamento__contains=departamento)
		serializer = FincaSerializer(fincas, many=True)
		return Response(serializer.data)

class BuscarFincaPorMunicipio(APIView):
	def get(self, request, municipio):
		fincas = Finca.objects.filter(municipio__contains=municipio)
		serializer = FincaSerializer(fincas, many=True)
		return Response(serializer.data)		

