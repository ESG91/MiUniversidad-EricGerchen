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
from Modulos.Academica import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),  # Ruta para la página de inicio
    path('formularioContacto/',views.formularioContacto,name='formularioContacto'),
    path('contactar/',views.contactar),
    path('estudiantes/',views.EstudianteListView.as_view(), name='estudiante_list'),
    path('estudiantes/create/',views.EstudianteCreateView.as_view(), name='estudiante_create'),
    path('estudiantes/<uuid:code>/',views.EstudianteDetailView.as_view(), name='estudiante_detail'),
    path('estudiantes/<uuid:pk>/update/', views.EstudianteUpdateView.as_view(), name='actualizar_estudiante'),
    path('estudiantes/<uuid:code>/delete/', views.EstudianteDeleteView.as_view(), name='estudiante_delete'),
    path('buscarEstudiantes/',views.buscar_estudiantes, name='buscar_estudiantes'),
    path('carrera/',views.CarreraListView.as_view(), name='carrera_list'),
    path('carrera/create/',views.CarreraCreateView.as_view(), name='carrera_create'),
    path('carrera/<uuid:code>/',views.CarreraDetailView.as_view(), name='carrera_detail'),
    path('carrera/<uuid:pk>/update/', views.CarreraUpdateView.as_view(), name='actualizar_carrera'),
    path('carrera/<uuid:code>/delete/', views.CarreraDeleteView.as_view(), name='carrera_delete'),
    path('buscarCarreras/',views.buscar_carreras, name='buscar_carreras'),
    path('about/',views.about_me, name='aboutMe'),
]