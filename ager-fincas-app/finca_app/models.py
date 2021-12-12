from django.db import models

# Create your models here.

# class User(models.Model):
# 	"""
# 		Tabla del Usuario aquí puede ir también PRODUCTOS
# 	"""
#     # id_usuario = models.BigAutoField(primary_key=True)
# 	id = models.BigAutoField(primary_key=True)
# 	username = models.CharField('Usuario', max_length = 80, unique=True)
#     # password = models.CharField('Password', max_length = 256)
#     # cedula = models.BigIntegerField('Cedula')
#     # email = models.EmailField('Email', max_length = 100)
#     # agricultor = models.BooleanField(default=False)
#     # comprador = models.BooleanField(default=False)
# 	def __str__(self):
# 		return self.username


class Finca(models.Model):
	"""
		Tabla de las Fincas
	"""
	id = models.BigAutoField(primary_key=True)
	nombre_finca = models.CharField('Nombre Finca', max_length = 45)
	direccion = models.CharField('Dirección', max_length = 80)
	telefono = models.BigIntegerField()
	ubicacion = models.CharField('Ubicación', max_length = 80)
	departamento = models.CharField('Departamento', max_length = 45)
	municipio = models.CharField('Municipio', max_length = 45)
	extension = models.CharField('Extensión', max_length = 80)
	propietario = models.CharField('Propietario', max_length = 45)
	# propietario = models.ForeignKey(
	# 	User, 
	# 	on_delete = models.CASCADE,
	# 	related_name = 'propietario'
	# 	)
	descripcion = models.CharField('Descripción', max_length = 250)
	def __str__(self):
		return self.nombre_finca