from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from .models import Estudiante, Carrera
from .forms import BusquedaEstudianteForm, BusquedaCarreraForm, ContactoForm, RegistroForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Vista para manejar el formulario de contacto
@login_required
def formularioContacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Enviar email usando los datos del formulario
            send_mail(
                form.cleaned_data['asunto'],
                form.cleaned_data['mensaje'],
                form.cleaned_data['email'],
                ['tuemail@example.com']
            )
            return redirect('gracias')
    else:
        form = ContactoForm()
    
    return render(request, 'formularioContacto.html', {'form': form})

# Vista simplificada para enviar un contacto
@login_required
def contactar(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Enviar email usando el formulario de contacto
            asunto = form.cleaned_data["asunto"]
            mensaje = f"{form.cleaned_data['mensaje']} / Email: {form.cleaned_data['email']}"
            send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, ["ERICGERCHEN@GMAIL.COM"], fail_silently=False)
            return render(request, "contactoExitoso.html")
    else:
        form = ContactoForm()

    return render(request, "formularioContacto.html", {"form": form})

# Vista para buscar estudiantes
@login_required
def buscar_estudiantes(request):
    form = BusquedaEstudianteForm()
    resultados = []

    if request.GET.get('criterio'):
        form = BusquedaEstudianteForm(request.GET)
        if form.is_valid():
            criterio = form.cleaned_data['criterio']
            resultados = Estudiante.objects.filter(Q(nombre__icontains=criterio) | Q(apellido__icontains=criterio))

    return render(request, 'estudiantes/buscar_estudiantes.html', {'form': form, 'resultados': resultados})

# Vista para buscar carreras
@login_required
def buscar_carreras(request):
    form = BusquedaCarreraForm()
    resultados = []

    if request.GET.get('criterio'):
        form = BusquedaCarreraForm(request.GET)
        if form.is_valid():
            criterio = form.cleaned_data['criterio']
            resultados = Carrera.objects.filter(Q(nombre__icontains=criterio) | Q(duracion__icontains=criterio))

    return render(request, 'carreras/buscar_carreras.html', {'form': form, 'resultados': resultados})

# Vista de página principal
@login_required
def index(request):
    return render(request, 'index.html')

# Vista de página 'Sobre mí'
@login_required
def about_me(request):
    return render(request, 'aboutMe.html')

# Vista genérica para crear un estudiante
class EstudianteCreateView(CreateView):
    model = Estudiante
    fields = ['dni', 'nombre', 'apellido', 'fechaNacimiento', 'email', 'sexo', 'carrera', 'vigencia']
    template_name = 'estudiantes/estudiante_form.html'
    success_url = reverse_lazy('estudiante_list')

# Vista genérica para listar estudiantes
class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'estudiantes/estudiante_list.html'
    context_object_name = 'estudiantes'

# Vista genérica para actualizar un estudiante
class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'fechaNacimiento', 'sexo', 'email', 'carrera', 'vigencia']
    template_name = 'estudiantes/estudiante_form.html'
    success_url = '/estudiantes/'

    def get_object(self, queryset=None):
        return get_object_or_404(Estudiante, code=self.kwargs.get('pk'))

# Vista genérica para eliminar un estudiante
class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = 'estudiantes/estudiante_confirm_delete.html'
    success_url = reverse_lazy('estudiante_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Estudiante, code=self.kwargs.get('code'))

# Vista genérica para mostrar detalles de un estudiante
class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = 'estudiantes/estudiante_detail.html'
    context_object_name = 'estudiante'

    def get_object(self):
        return get_object_or_404(Estudiante, code=self.kwargs.get('code'))

# Vista genérica para crear una carrera
class CarreraCreateView(CreateView):
    model = Carrera
    fields = ['codigo', 'nombre', 'duracion']
    template_name = 'carreras/carrera_form.html'
    success_url = reverse_lazy('carrera_list')

# Vista genérica para listar carreras
class CarreraListView(ListView):
    model = Carrera
    template_name = 'carreras/carrera_list.html'
    context_object_name = 'carreras'

# Vista genérica para actualizar una carrera
class CarreraUpdateView(UpdateView):
    model = Carrera
    fields = ['codigo', 'nombre', 'duracion']
    template_name = 'carreras/carrera_form.html'
    success_url = '/carrera/'

    def get_object(self, queryset=None):
        return get_object_or_404(Carrera, code=self.kwargs.get('pk'))

# Vista genérica para eliminar una carrera
class CarreraDeleteView(DeleteView):
    model = Carrera
    template_name = 'carreras/carrera_confirm_delete.html'
    success_url = reverse_lazy('carrera_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Carrera, code=self.kwargs.get('code'))

# Vista genérica para mostrar detalles de una carrera
class CarreraDetailView(DetailView):
    model = Carrera
    template_name = 'carreras/carrera_detail.html'
    context_object_name = 'carrera'

    def get_object(self):
        return get_object_or_404(Carrera, code=self.kwargs.get('code'))

# Vista para el registro de usuarios
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegistroForm()
    
    return render(request, 'registration/registro.html', {'form': form})
