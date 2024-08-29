## Autor
Eric Gerchen

## Proyecto de Administración de Universidad
Este proyecto es una aplicación web desarrollada con Django, diseñada para administrar una universidad. La aplicación permite gestionar información relacionada con carreras, estudiantes, cursos, y matrículas. Además, incluye funcionalidad para enviar correos electrónicos a los estudiantes.

## Estructura del Proyecto
El proyecto está organizado en módulos que representan diferentes aspectos de la universidad:

## 1. Carrera
Modelo: Carrera
Descripción: Representa una carrera universitaria. Cada carrera tiene un código único, un nombre, y una duración (en años).
Campos:
codigo: Código alfanumérico de 3 caracteres (PK).
nombre: Nombre de la carrera.
duracion: Duración de la carrera en años (por defecto 5).
## 2. Estudiante
Modelo: Estudiante
Descripción: Representa un estudiante inscrito en la universidad. Cada estudiante tiene un DNI único, nombre, apellido, fecha de nacimiento, sexo, y una carrera asociada.
Campos:
dni: Documento Nacional de Identidad (PK).
nombre: Nombre del estudiante.
apellido: Apellido del estudiante.
fechaNacimiento: Fecha de nacimiento del estudiante.
sexo: Género del estudiante (Masculino o Femenino).
carrera: Relación ForeignKey a Carrera.
vigencia: Indica si el estudiante está activo o no (por defecto True).
## 3. Curso
Modelo: Curso
Descripción: Representa un curso ofrecido por la universidad. Cada curso tiene un código único, un nombre, y un docente asignado.
Campos:
codigo: Código alfanumérico de 6 caracteres (PK).
nombre: Nombre del curso.
docente: Nombre del docente a cargo del curso.
## 4. Matricula
Modelo: Matricula
Descripción: Representa la matrícula de un estudiante en un curso. Cada matrícula registra un estudiante, un curso, y la fecha en que se realizó la matrícula.
Campos:
id: ID autogenerado (PK).
estudiante: Relación ForeignKey a Estudiante.
curso: Relación ForeignKey a Curso.
fechaMatricula: Fecha y hora de la matrícula (generada automáticamente).

## Funcionalidad Principal
## 1. Gestión de Estudiantes
Permite agregar, editar, y eliminar estudiantes.
Permite buscar estudiantes por nombre o apellido mediante un formulario de búsqueda, con validación para asegurarse de que el criterio de búsqueda no esté vacío y que solo contenga letras.
## 2. Matrícula de Cursos
Los estudiantes pueden ser matriculados en uno o más cursos.
Validación para evitar la matrícula duplicada de un estudiante en el mismo curso.
## 3. Envío de Correos Electrónicos
La aplicación incluye funcionalidad para enviar correos electrónicos a los estudiantes, notificándoles sobre su matrícula o información relevante.
## 1. Gestión de Carreras
Permite agregar, editar, y eliminar carreras.
Permite buscar carreras mediante un formulario de búsqueda, con validación para asegurarse de que el criterio de búsqueda no esté vacío y que solo contenga letras.