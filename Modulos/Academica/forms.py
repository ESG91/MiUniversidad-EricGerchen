from django import forms
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Clase base para formularios de búsqueda
class BaseBusquedaForm(forms.Form):
    criterio = forms.CharField(label='Buscar', max_length=100)

    # Validación común para los campos 'criterio'
    def clean_criterio(self):
        criterio = self.cleaned_data.get('criterio')

        # Verificar que solo contenga letras
        if not re.match(r'^[a-zA-Z\sáéíóúÁÉÍÓÚñÑ]+$', criterio):
            raise ValidationError('Este campo solo puede contener letras.')

        return criterio


# Formularios específicos heredan de la clase base
class BusquedaEstudianteForm(BaseBusquedaForm):
    pass


class BusquedaCarreraForm(BaseBusquedaForm):
    pass


class ContactoForm(forms.Form):
    asunto = forms.CharField(label='Asunto', max_length=100)
    email = forms.EmailField(label='Email')
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))

    # Validación personalizada para el asunto
    def clean_asunto(self):
        asunto = self.cleaned_data.get('asunto')
        return asunto  # Ya se valida que no esté vacío al ser un CharField requerido

    # Validación personalizada para el email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email  # EmailField ya valida el formato

    # Validación personalizada para el mensaje
    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')
        return mensaje  # Ya se valida que no esté vacío al ser un CharField requerido


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
