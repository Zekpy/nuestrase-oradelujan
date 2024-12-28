from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    LUGAR_CHOICES = [
        ('Sede', 'Sede'),
        ('Subsede', 'Subsede'),
        ('Anexo', 'Anexo'),
    ]
    
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    matricula_maxima = models.PositiveIntegerField()
    lugar = models.CharField(max_length=50, choices=LUGAR_CHOICES, default='Sede')
    proyecto = models.FileField(upload_to='proyectos/', blank=True, null=True)  # Para cargar el archivo PDF
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cursos', limit_choices_to={'groups__name': 'Instructores'})
    
    @property
    def total_horas(self):
        return sum(modulo.horas for modulo in self.modulos.all())

    @property
    def inscritos(self):
        return self.alumnos.count()  # Cuenta el número de alumnos inscritos

    @property
    def lugares_disponibles(self):
        return self.matricula_maxima - self.inscritos  # Resta los inscritos de la matrícula máxima

    def __str__(self):
        return self.nombre

class Modulo(models.Model):
    curso = models.ForeignKey(Curso, related_name='modulos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    horas = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.horas} horas"

class Inscripcion(models.Model):
    curso = models.ForeignKey(Curso, related_name='inscripciones', on_delete=models.CASCADE)
    estudiante = models.ForeignKey(User, related_name='inscripciones', on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Alumno'})
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudiante.username} inscrito en {self.curso.nombre}"


class Alumno(models.Model):
    ESTUDIOS_CHOICES = [
        ('Primaria', 'Primaria'),
        ('Secundaria', 'Secundaria'),
    ]

    dni = models.CharField(max_length=20, unique=True)  # DNI
    cuil = models.CharField(max_length=20, unique=True)  # CUIL
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular_1 = models.CharField(max_length=15)  # Primer número de celular
    celular_2 = models.CharField(max_length=15)  # Segundo número de celular
    email = models.EmailField(unique=True)
    foto_dni_frente = models.ImageField(upload_to='fotos_dni/frente/', blank=True, null=True)  # Foto del DNI (frente)
    foto_dni_reversa = models.ImageField(upload_to='fotos_dni/reversa/', blank=True, null=True)  # Foto del DNI (reversa)
    estudios_maximos = models.ImageField(upload_to='fotos_estudios/reversa/', blank=True, null=True)  # Foto del DNI (reversa)
    curso = models.ForeignKey(Curso, related_name='alumnos', on_delete=models.CASCADE)  # Relación con Curso
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.curso.nombre}"
    @property
    def cursos_inscritos(self):
        return self.curso