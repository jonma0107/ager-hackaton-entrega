"""ager_finca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('finca_app.urls')),
# ]
from django.urls import path, include
from finca_app import views

urlpatterns = [
    path('finca/list/', views.FincaListado.as_view()),
    path('finca/<int:pk>/', views.FincaBuscarPorId.as_view()),
    path('finca/registrar/', views.FincaRegistrar.as_view()),
    path('finca/editar/<int:pk>/', views.FincaEditar.as_view()),
    path('finca/eliminar/<int:pk>/', views.FincaEliminar.as_view()),

    path('finca/buscar/nombre/<str:nombre_finca>', views.BuscarFincaPorNombreFinca.as_view()),
    path('finca/buscar/propietario/<str:propietario>', views.BuscarFincaPorPropietario.as_view()),
    path('finca/buscar/departamento/<str:departamento>', views.BuscarFincaPorDepartamento.as_view()),
    path('finca/buscar/municipio/<str:municipio>', views.BuscarFincaPorMunicipio.as_view()),

]