from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .cursosform import ModuloForm, CursoForm,AlumnoForm
from django.contrib import messages
from .models import Curso
@login_required  # Asegura que solo usuarios autenticados accedan a esta vista
def home(request):
    # Redirige al panel de administración si el usuario es staff
    if request.user.is_staff:
        return redirect('/admin/')  # Redirige al panel de administración si es staff
    return render(request, 'inicio/index.html')  # Renderiza la página principal para otros usuarios


@login_required
def dashboard(request):
    user = request.user

    # Comprobamos el grupo del usuario y redirigimos al dashboard correspondiente
    if user.groups.filter(name="alumnos").exists():
        # Accedemos al modelo Alumno a través del usuario
        alumno = getattr(user, 'alumnos', None)
        if alumno:
            cursos = alumno.cursos_inscritos
            return render(request, "inicio/dashboard_alumno.html", {'cursos': cursos})
        else:
            # Manejo de error si no existe el objeto Alumno
            return render(request, "inicio/dashboard_error.html", {'error': 'Alumno no encontrado'})
   
    elif user.groups.filter(name="Instructor").exists():
        return render(request, "inicio/dashboard_instructor.html")
    elif user.groups.filter(name="Directivo").exists():
        return render(request, "inicio/dashboard_directivo.html")
    else:
        return render(request, "inicio/dashboard_default.html")

    





@login_required
def perfil(request):
    user = request.user
    group_names = user.groups.values_list('name', flat=True)
    return render(request, 'account/profile.html', {'user': user, 'group_names': group_names})



@login_required
def crear_curso(request):
    if request.user.groups.filter(name="Instructores").exists():  # Verifica si el usuario es un instructor
        if request.method == 'POST':
            form = CursoForm(request.POST)
            if form.is_valid():
                curso = form.save(commit=False)
                curso.instructor = request.user  # Asigna al instructor que está creando el curso
                curso.save()

                # Guardar los módulos si se han añadido
                modulo_formset = ModuloForm(request.POST, instance=curso)
                if modulo_formset.is_valid():
                    modulo_formset.save()

                messages.success(request, "Curso creado exitosamente")
                return redirect('../dashboard')  # Redirige al escritorio del instructor
        else:
            form = CursoForm()

        return render(request, 'inicio/crear_curso.html', {'form': form})
    else:
        messages.error(request, "No tienes permisos para crear un curso")
        return redirect('dashboard')  # Redirige a un lugar seguro si no es instructor
    


@login_required
def registrar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el alumno en la base de datos
            return redirect('registro_exitoso')  # Redirigir a una página de éxito o confirmación
        else:
            # Si el formulario no es válido, se renderiza nuevamente con los errores
            return render(request, 'inicio/registro_alumno.html', {'form': form})
    else:
        form = AlumnoForm()
        return render(request, 'inicio/registro_alumno.html', {'form': form})
    
def curso_exitoso(request):
    return render(request, 'inicio/registro_exitoso.html')  # O lo que sea que quieras hacer en esta vista