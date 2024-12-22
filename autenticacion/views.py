from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm

# Vista de Registro
def registro(request):
    # Verifica si el método de la solicitud es POST (cuando el usuario envía el formulario)
    if request.method == "POST":
        # Crea un formulario con los datos enviados por el usuario (request.POST y request.FILES para archivos)
        form = RegistroForm(request.POST, request.FILES)
        
        # Verifica si el formulario es válido (si los datos cumplen con las reglas definidas en el formulario)
        if form.is_valid():
            # Guarda los datos del formulario en la base de datos
            form.save()
            
            # Muestra un mensaje de éxito
            messages.success(request, "¡Te has registrado exitosamente!")
            
            # Redirige al usuario a la página de inicio de sesión después de un registro exitoso
            return redirect('iniciar_sesion')  # Redirige a la página de login o la que prefieras
    else:
        # Si el método no es POST, crea un formulario vacío para que el usuario lo complete
        form = RegistroForm()

    # Renderiza la plantilla 'registro.html' y pasa el formulario al contexto
    return render(request, 'autenticacion/registro.html', {'form': form})

# Vista de Inicio de Sesión
def iniciar_sesion(request):
    # Renderiza la plantilla de inicio de sesión (sin datos adicionales)
    return render(request, 'autenticacion/iniciar_sesion.html')

# Vista de Inicio (Página principal)
def inicio(request):
    # Renderiza la plantilla 'index.html' como la página de inicio o la página principal
    return render(request, 'autenticacion/index.html')
