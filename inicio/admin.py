from django.contrib import admin
from .models import Curso, Modulo
from .models import Alumno
# Definir el InlineModelAdmin para los módulos
class ModuloInline(admin.TabularInline):
    model = Modulo
    extra = 1  # Número de formularios vacíos adicionales que se mostrarán
    fields = ['nombre', 'horas']  # Campos que se mostrarán en la interfaz de administración

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'matricula_maxima', 'inscritos', 'lugares_disponibles')
    # Aquí estamos añadiendo las propiedades "inscritos" y "lugares_disponibles" a la vista de la lista de cursos





class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('dni', 'cuil', 'nombre', 'apellido', 'email', 'estudios_maximos', 'celular_1', 'celular_2', 'curso')
    search_fields = ('dni', 'cuil', 'nombre', 'apellido', 'email')
    list_filter = ('curso', 'estudios_maximos')
    ordering = ('apellido', 'nombre')
    list_per_page = 20

    # Para mostrar las fotos de DNI en miniatura
    def get_foto_dni_frente(self, obj):
        if obj.foto_dni_frente:
            return f'<img src="{obj.foto_dni_frente.url}" width="50" height="50" />'
        return "No disponible"
    get_foto_dni_frente.allow_tags = True
    get_foto_dni_frente.short_description = 'Foto DNI (Frente)'

    def get_foto_dni_reversa(self, obj):
        if obj.foto_dni_reversa:
            return f'<img src="{obj.foto_dni_reversa.url}" width="50" height="50" />'
        return "No disponible"
    get_foto_dni_reversa.allow_tags = True
    get_foto_dni_reversa.short_description = 'Foto DNI (Reversa)'

    # Agregar las fotos de DNI a la vista de lista
    list_display = ('dni', 'cuil', 'nombre', 'apellido', 'email', 'estudios_maximos', 'celular_1', 'celular_2', 'get_foto_dni_frente', 'get_foto_dni_reversa', 'curso')

admin.site.register(Alumno, AlumnoAdmin)
# Registrar los modelos en el admin
admin.site.register(Curso, CursoAdmin)
admin.site.register(Modulo)