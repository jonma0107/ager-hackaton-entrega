from django.conf import settings
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.views import APIView

from autenticationApp.models      import User
from autenticationApp.serializers import UserSerializer

class UserView(views.APIView):

    def authenticate(self,request, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            return 0
        else:
            return valid_data['user_id']
    
    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        tokenData = {"username":request.data["username"],
                     "password":request.data["password"]}

        print(tokenData)

        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
    
    def put(self,request, *args, **kwargs):
        user_id = self.authenticate(request, *args, **kwargs)
        if user_id == 0:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        else:

            user = User.objects.get(id=user_id)
            user_serializer = UserSerializer(user,data=request.data)

            if user_serializer.is_valid(raise_exception=True):
                user_serializer.save()
                stringResponse = {'detail':'Usuario actulizado'}
                return Response(stringResponse, status=status.HTTP_201_CREATED)
            else:
                stringResponse = {'detail':'Usuario no actulizado'}
                return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)


class BuscarUserPorUsername(APIView):
    def get(self, request, username):
        usuarios = User.objects.filter(username__contains=username)
        serializer = UserSerializer(usuarios, many=True)
        return Response(serializer.data)

class BuscarUserPorNombre(APIView):
    def get(self, request, nombre):
        nombres = User.objects.filter(nombre__contains=nombre)
        serializer = UserSerializer(nombres, many=True)
        return Response(serializer.data)

class BuscarUserPorApellido(APIView):
    def get(self, request, apellido):
        apellidos = User.objects.filter(apellidos__contains=apellido)
        serializer = UserSerializer(apellidos, many=True)
        return Response(serializer.data)

class BuscarUserPorCedula(APIView):
    def get(self, request, cedula):
        cedulas = User.objects.filter(cedula__contains=cedula)
        serializer = UserSerializer(cedulas, many=True)
        return Response(serializer.data)

class BuscarUserPorRol(APIView):
    def get(self, request, rol):
        roles = User.objects.filter(rol__contains=rol)
        serializer = UserSerializer(roles, many=True)
        return Response(serializer.data)                    