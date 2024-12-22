from django.contrib.auth.models import AbstractUser
from django.db import models

# Definición del modelo 'Usuario', que extiende de 'AbstractUser'
class Usuario(AbstractUser):
    # Campos adicionales
    nombre_completo = models.CharField(max_length=150, verbose_name="Nombre Completo")
    foto_perfil = models.ImageField(upload_to="fotos_perfil/", null=True, blank=True, verbose_name="Foto de Perfil")
    celular = models.CharField(max_length=15, verbose_name="Número de Celular", null=True, blank=True)
    email = models.EmailField(null=False)
    celular = models.CharField(max_length=10)

    # Campo para roles
    ROLES = [
        ("estudiante", "Estudiante"),
        ("instructor", "Instructor"),
        ("directivo", "Directivo"),
    ]
    rol = models.CharField(
        max_length=20,
        choices=ROLES,
        default="estudiante",
        verbose_name="Rol"
    )
    
    # Campo para confirmar roles especiales
    es_confirmado = models.BooleanField(default=False, verbose_name="¿Confirmado por el Administrador?")

    # Método para mostrar el nombre de usuario y su rol
    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"
