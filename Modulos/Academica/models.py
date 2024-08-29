from django.db import models
from django.core.exceptions import ValidationError

class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

    def clean(self):
        if self.duracion <= 0:
            raise ValidationError('La duración de la carrera debe ser un número positivo mayor que 0.')

    def __str__(self) -> str:
        return f"{self.nombre} (Duración: {self.duracion} año(s))"

class Estudiante(models.Model):
    dni = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='M')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def nombreCompleto(self):
        return f"{self.apellido}, {self.nombre}"

    def __str__(self) -> str:
        estadoEstudiante = "VIGENTE" if self.vigencia else "DE BAJA"
        return f"{self.nombreCompleto()} / Carrera: {self.carrera} / {estadoEstudiante}"
    
    def get_sexo_display(self):
        return dict(self.sexos).get(self.sexo, 'Desconocido')

    def get_estado_vigencia(self):
        return "Vigente" if self.vigencia else "De baja"

class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    docente = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.nombre} ({self.codigo}) / Docente: {self.docente}"

class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if Matricula.objects.filter(estudiante=self.estudiante, curso=self.curso).exists():
            raise ValidationError('El estudiante ya está matriculado en este curso.')

    def __str__(self) -> str:
        if self.estudiante.sexo == 'F':
                 letraSexo = "a"
        else:
                letraSexo = "o"
        fecMat = self.fechaMatricula.strftime("%A %d/%m/%Y %H:%M:%S")
        return f"{self.estudiante.nombreCompleto()} matriculad{letraSexo} en el curso {self.curso} / Fecha: {fecMat}"
