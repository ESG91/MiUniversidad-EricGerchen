from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import Estudiante,Carrera
from .forms import BusquedaEstudianteForm,BusquedaCarreraForm,ContactoForm
from django.db.models import Q
from django.shortcuts import get_object_or_404

# Create your views here.

def formularioContacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            asunto = form.cleaned_data['asunto']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            # Enviar el email
            send_mail(asunto, mensaje, email, ['tuemail@example.com'])
            return redirect('gracias')
    else:
        form = ContactoForm()

    return render(request, 'formularioContacto.html', {'form': form})

def contactar(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            asunto = form.cleaned_data["asunto"]
            mensaje = form.cleaned_data["mensaje"] + " / Email: " + form.cleaned_data["email"]
            email_desde = settings.EMAIL_HOST_USER
            email_para = ["ERICGERCHEN@GMAIL.COM"]
            
            send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
            return render(request, "contactoExitoso.html")
    else:
        form = ContactoForm()

    return render(request, "formularioContacto.html", {"form": form})

def buscar_estudiantes(request):
    form = BusquedaEstudianteForm()
    resultados = []

    if request.method == 'GET' and 'criterio' in request.GET:
        form = BusquedaEstudianteForm(request.GET)
        if form.is_valid():
            criterio = form.cleaned_data['criterio']
            resultados = Estudiante.objects.filter(
                Q(nombre__icontains=criterio) | Q(apellido__icontains=criterio)
            )

    return render(request, 'buscar_estudiantes.html', {'form': form, 'resultados': resultados})


def detalle_estudiante(request, code):
    estudiante = get_object_or_404(Estudiante, code=code)
    return render(request, 'detalle_estudiante.html', {'estudiante': estudiante})


def buscar_carreras(request):
    form = BusquedaCarreraForm()
    resultados = []

    if request.method == 'GET' and 'criterio' in request.GET:
        form = BusquedaCarreraForm(request.GET)
        if form.is_valid():
            criterio = form.cleaned_data['criterio']
            resultados = Carrera.objects.filter(
                Q(nombre__icontains=criterio) | Q(duracion__icontains=criterio)
            )

    return render(request, 'buscar_carreras.html', {'form': form, 'resultados': resultados})

def detalle_carrera(request, code):
    carrera = get_object_or_404(Carrera, code=code)
    return render(request, 'detalle_carrera.html', {'carrera': carrera})

def index(request):
    return render(request, 'index.html')

def about_me(request):
    return render(request, 'aboutMe.html')

