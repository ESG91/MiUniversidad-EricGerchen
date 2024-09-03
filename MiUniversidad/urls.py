"""
URL configuration for MiUniversidad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Modulos.Academica.views import formularioContacto,contactar,buscar_estudiantes,buscar_carreras,index,detalle_estudiante,detalle_carrera

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),  # Ruta para la página de inicio
    path('formularioContacto/',formularioContacto,name='formularioContacto'),
    path('contactar/',contactar),
    path('buscarEstudiantes/',buscar_estudiantes, name='buscar_estudiantes'),
    path('detalleEstudiante/<uuid:code>/',detalle_estudiante, name='detalle_estudiante'),
    path('buscarCarreras/',buscar_carreras, name='buscar_carreras'),
    path('detalleCarrera/<uuid:code>/',detalle_carrera, name='detalle_carrera'),
]