from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import ActualizarPerfilForm
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
    if request.method == "POST":
        usuario = request.POST.get('username')  # Cambiado de 'username' a 'usuario'
        password = request.POST.get('password')

        user = authenticate(request, username=usuario, password=password)  # username aquí se refiere al campo del modelo
        if user is not None:
            login(request, user)
            messages.success(request, "Inicio de sesión exitoso.")
            return redirect('perfil_usuario')  # Redirige a la página de inicio
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
            return render(request, 'autenticacion/iniciar_sesion.html')

    return render(request, 'autenticacion/iniciar_sesion.html')



@login_required
def perfil(request):
    usuario = request.user  # Obtiene el usuario autenticado
    if request.method == 'POST':
        form = ActualizarPerfilForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()  # Guarda los datos del formulario
            return redirect('perfil_usuario')  # Redirige a la misma página después de guardar los cambios
    else:
        form = ActualizarPerfilForm(instance=usuario)  # Carga el formulario con los datos del usuario

    return render(request, 'autenticacion/perfil_usuario.html', {'usuario': usuario, 'form': form})



def inicio (request):
     return render(request, 'autenticacion/index.html')