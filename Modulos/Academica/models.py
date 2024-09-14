from django.db import models
from django.core.exceptions import ValidationError
import uuid

class Carrera(models.Model):
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

    # Validación para duración
    def clean(self):
        if self.duracion <= 0:
            raise ValidationError('La duración de la carrera debe ser un número positivo mayor que 0.')

    # Representación en string de la carrera
    def __str__(self) -> str:
        return f"{self.nombre} (Duración: {self.duracion} año(s))"


class Estudiante(models.Model):
    SEXOS = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]

    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    dni = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    email = models.EmailField(max_length=254, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXOS, default='M')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    # Método para obtener el nombre completo
    def nombreCompleto(self):
        return f"{self.apellido}, {self.nombre}"

    # Representación en string del estudiante
    def __str__(self) -> str:
        estadoEstudiante = "VIGENTE" if self.vigencia else "DE BAJA"
        return f"{self.nombreCompleto()} / Carrera: {self.carrera} / {estadoEstudiante}"
    
    # Mostrar el sexo en formato legible
    def get_sexo_display(self):
        return dict(self.SEXOS).get(self.sexo, 'Desconocido')

    # Mostrar el estado de vigencia del estudiante
    def get_estado_vigencia(self):
        return "Vigente" if self.vigencia else "De baja"


class Curso(models.Model):
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    docente = models.CharField(max_length=100)

    # Representación en string del curso
    def __str__(self) -> str:
        return f"{self.nombre} ({self.codigo}) / Docente: {self.docente}"


class Matricula(models.Model):
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)

    # Validación para evitar duplicación de matriculación
    def clean(self):
        if Matricula.objects.filter(estudiante=self.estudiante, curso=self.curso).exists():
            raise ValidationError('El estudiante ya está matriculado en este curso.')

    # Representación en string de la matrícula
    def __str__(self) -> str:
        letraSexo = "a" if self.estudiante.sexo == 'F' else "o"
        fecMat = self.fechaMatricula.strftime("%A %d/%m/%Y %H:%M:%S")
        return f"{self.estudiante.nombreCompleto()} matriculad{letraSexo} en el curso {self.curso} / Fecha: {fecMat}"
