from django.urls import path
from .views import home, perfil,dashboard,crear_curso,registrar_alumno,curso_exitoso

  
urlpatterns = [
    path('',home,name='index'),
    path('profile/',perfil , name='profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('crear-curso/', crear_curso, name='crear_curso'),
    path('registro-alumno/', registrar_alumno, name='registro_alumno'),
    path('registro_exitoso/', curso_exitoso, name='registro_exitoso'),


]