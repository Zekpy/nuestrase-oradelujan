from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Usuario
from django.contrib.auth.forms import UserChangeForm

# Formulario para el registro de nuevos usuarios
class RegistroForm(UserCreationForm):
    # Campo para el nombre completo del usuario
    # 'CharField' se usa para ingresar texto. 
    # 'max_length=150' establece que el nombre no puede tener más de 150 caracteres.
    # 'required=True' hace que este campo sea obligatorio.
    # 'label="Nombre Completo"' define el texto que se mostrará junto al campo en el formulario.
    nombre_completo = forms.CharField(max_length=150, required=True, label="Nombre Completo")
    
    # Campo para la foto de perfil del usuario
    # 'ImageField' se usa para cargar imágenes. 
    # 'required=False' indica que este campo es opcional.
    # 'label="Foto de Perfil"' define el texto que se mostrará junto al campo en el formulario.
    foto_perfil = forms.ImageField(required=False, label="Foto de Perfil")
    
    # Campo para el número de celular del usuario
    # 'CharField' se usa para ingresar texto (en este caso, un número de celular).
    # 'max_length=15' establece que el número de celular no puede tener más de 15 caracteres.
    # 'required=True' hace que este campo sea obligatorio.
    # 'label="Celular"' define el texto que se mostrará junto al campo en el formulario.
    celular = forms.CharField(max_length=15, required=True, label="Celular")
    
    # Campo para el correo electrónico del usuario
    # 'EmailField' es un tipo de campo específico para correos electrónicos. 
    # 'required=True' hace que este campo sea obligatorio.
    # 'label="Correo Electrónico"' define el texto que se mostrará junto al campo en el formulario.
    email = forms.EmailField(required=True, label="Correo Electrónico")
    
    # Campo para seleccionar el rol del usuario
    # 'ChoiceField' permite seleccionar un valor de una lista de opciones predefinidas.
    # 'choices=Usuario.ROLES' es la lista de opciones que se definen en el modelo 'Usuario'.
    # 'required=True' hace que este campo sea obligatorio.
    # 'label="Rol"' define el texto que se mostrará junto al campo en el formulario.
    rol = forms.ChoiceField(choices=Usuario.ROLES, required=True, label="Rol")

    # Método de validación para el campo 'email'
    # 'clean_email' es una función personalizada que valida si el correo electrónico ya está registrado en la base de datos.
    def clean_email(self):
        # 'self.cleaned_data.get('email')' obtiene el valor del campo 'email' después de la limpieza del formulario.
        email = self.cleaned_data.get('email')
        
        # Verifica si ya existe un usuario con el mismo correo electrónico en la base de datos.
        # 'Usuario.objects.filter(email=email).exists()' consulta si el correo ya está registrado.
        if Usuario.objects.filter(email=email).exists():
            # Si el correo ya está registrado, se lanza un 'ValidationError' con un mensaje de error.
            raise ValidationError("Este correo electrónico ya está registrado.")
        
        # Si el correo es válido, se devuelve el valor del correo.
        return email

    # Clase Meta para definir la configuración adicional del formulario
    class Meta:
        # 'model = Usuario' especifica que este formulario está relacionado con el modelo 'Usuario'.
        # Esto significa que los datos ingresados en el formulario se guardarán en la tabla correspondiente al modelo 'Usuario'.
        model = Usuario
        
        # 'fields' define los campos que aparecerán en el formulario.
        # Los campos 'username', 'nombre_completo', 'email', 'celular', 'foto_perfil', 'rol', 'password1' y 'password2' 
        # son los campos que estarán disponibles en el formulario de registro.
        fields = ('username', 'nombre_completo', 'email', 'celular', 'foto_perfil', 'rol', 'password1', 'password2')




class ActualizarPerfilForm(UserChangeForm):
    password = None  # Ocultar el campo de contraseña

    class Meta:
        model = Usuario  # Tu modelo de usuario
        fields = ('username', 'nombre_completo', 'email', 'celular', 'foto_perfil')  # Campos a editar
        widgets = {
            'foto_perfil': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
        }
