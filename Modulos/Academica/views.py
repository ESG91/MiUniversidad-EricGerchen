from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import Estudiante,Carrera
from .forms import BusquedaEstudianteForm,BusquedaCarreraForm,ContactoForm
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

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

    return render(request, 'estudiantes/buscar_estudiantes.html', {'form': form, 'resultados': resultados})

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

    return render(request, 'carreras/buscar_carreras.html', {'form': form, 'resultados': resultados})

def index(request):
    return render(request, 'index.html')

def about_me(request):
    return render(request, 'aboutMe.html')

class EstudianteCreateView(CreateView):
    model = Estudiante
    fields = ['dni', 'nombre', 'apellido', 'fechaNacimiento', 'email','sexo', 'carrera', 'vigencia']
    template_name = 'estudiantes/estudiante_form.html'
    success_url = reverse_lazy('estudiante_list')

class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'estudiantes/estudiante_list.html'
    context_object_name = 'estudiantes'

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'fechaNacimiento','sexo', 'email','carrera', 'vigencia']
    template_name = 'estudiantes/estudiante_form.html'
    success_url = '/estudiantes/'

    def get_object(self, queryset=None):
        # Obtener el UUID del parámetro 'pk'
        code = self.kwargs.get('pk')
        try:
            return Estudiante.objects.get(code=code)
        except Estudiante.DoesNotExist:
            raise Http404("Estudiante no encontrado")

class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = 'estudiantes/estudiante_confirm_delete.html'
    success_url = reverse_lazy('estudiante_list')

    def get_object(self, queryset=None):
        # Obtén el 'code' de los argumentos de la URL
        code = self.kwargs.get('code')
        # Busca el estudiante con el 'code' especificado
        return Estudiante.objects.get(code=code)

class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = 'estudiantes/estudiante_detail.html'
    context_object_name = 'estudiante'
    
    def get_object(self):
        code = self.kwargs.get('code')
        return get_object_or_404(Estudiante, code=code) 

class CarreraCreateView(CreateView):
    model = Carrera
    fields = ['codigo', 'nombre', 'duracion']
    template_name = 'carreras/carrera_form.html'
    success_url = reverse_lazy('carrera_list')

class CarreraListView(ListView):
    model = Carrera
    fields = ['nombre', 'duracion']
    template_name = 'carreras/carrera_list.html'
    context_object_name = 'carreras'

class CarreraUpdateView(UpdateView):
    model = Carrera
    fields = ['codigo', 'nombre', 'duracion']
    template_name = 'carreras/carrera_form.html'
    success_url = '/carrera/'

    def get_object(self, queryset=None):
        # Obtener el UUID del parámetro 'pk'
        code = self.kwargs.get('pk')
        try:
            return Carrera.objects.get(code=code)
        except Carrera.DoesNotExist:
            raise Http404("carreras no encontrada")

class CarreraDeleteView(DeleteView):
    model = Carrera
    template_name = 'carreras/carrera_confirm_delete.html'
    success_url = reverse_lazy('carrera_list')

    def get_object(self, queryset=None):
        # Obtén el 'code' de los argumentos de la URL
        code = self.kwargs.get('code')
        # Busca el estudiante con el 'code' especificado
        return Carrera.objects.get(code=code)

class CarreraDetailView(DetailView):
    model = Carrera
    template_name = 'carreras/carrera_detail.html'
    context_object_name = 'carrera'
    
    def get_object(self):
        code = self.kwargs.get('code')
        return get_object_or_404(Carrera, code=code) 
