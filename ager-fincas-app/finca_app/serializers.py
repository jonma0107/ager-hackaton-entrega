from rest_framework import serializers
from .models import Finca

# Serializadores
# class UserSerializer(serializers.ModelSerializer):
# 	"""
# 		Serializador del usuario

# 	"""

# 	class Meta:
# 		model = User
# 		fields = '__all__'


# class FincaConDatosDelUsuarioAsociadoSerializer(serializers.ModelSerializer):
# 	"""
# 		Serializador de las fincas con su usuario

# 	"""
# 	propietario = UserSerializer(read_only=True)
# 	class Meta:
# 		model = Finca
# 		fields = '__all__'


class FincaSerializer(serializers.ModelSerializer):
	"""

		Serializador sólo de las Fincas

	"""
	class Meta:
		model = Finca
		fields = '__all__'

	