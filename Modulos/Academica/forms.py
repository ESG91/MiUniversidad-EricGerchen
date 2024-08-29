from django import forms
from django.core.exceptions import ValidationError
import re

class BusquedaEstudianteForm(forms.Form):
    criterio = forms.CharField(label='Buscar', max_length=100)

    def clean_criterio(self):
        criterio = self.cleaned_data.get('criterio')

        # Verificar que no esté vacío
        if not criterio:
            raise ValidationError('Este campo no puede estar vacío.')

        # Verificar que solo contenga letras
        if not re.match(r'^[a-zA-Z\sáéíóúÁÉÍÓÚñÑ]+$', criterio):
            raise ValidationError('Este campo solo puede contener letras.')

        return criterio
    

class BusquedaCarreraForm(forms.Form):
    criterio = forms.CharField(label='Buscar', max_length=100)

    def clean_criterio(self):
        criterio = self.cleaned_data.get('criterio')

        # Verificar que no esté vacío
        if not criterio:
            raise ValidationError('Este campo no puede estar vacío.')

        # Verificar que solo contenga letras
        if not re.match(r'^[a-zA-Z\sáéíóúÁÉÍÓÚñÑ]+$', criterio):
            raise ValidationError('Este campo solo puede contener letras.')

        return criterio    

class ContactoForm(forms.Form):
    asunto = forms.CharField(label='Asunto', max_length=100)
    email = forms.EmailField(label='Email')
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))

    def clean_asunto(self):
        asunto = self.cleaned_data.get('asunto')
        if not asunto:
            raise ValidationError("El campo asunto no puede estar vacío.")
        return asunto

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("El campo email no puede estar vacío.")
        return email

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')
        if not mensaje:
            raise ValidationError("El campo mensaje no puede estar vacío.")
        return mensaje