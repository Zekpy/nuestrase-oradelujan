from django import forms
from .models import Curso, Modulo,Alumno

class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ['nombre', 'curso', 'horas']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'lugar', 'proyecto', 'fecha_inicio', 'fecha_fin','matricula_maxima']
    
    # Campos adicionales para los módulos
    modulos = forms.inlineformset_factory(Curso, Modulo, form=ModuloForm, extra=1, can_delete=True)




class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = [
             
            'dni', 
            'cuil', 
            'nombre', 
            'apellido', 
            'celular_1', 
            'celular_2', 
            'email', 
            'foto_dni_frente', 
            'foto_dni_reversa', 
            'estudios_maximos',
            'curso'
        ]
        
    def clean_curso(self):
        curso = self.cleaned_data.get('curso')
        alumno = self.instance  # Si el formulario está editando un alumno, usamos la instancia del alumno

        # Verificar si el alumno ya está inscrito en algún curso
        if Alumno.objects.filter(curso=curso).exists():
            raise forms.ValidationError('Ya estás inscrito en un curso. No puedes inscribirte en más de uno.')
        
        return curso

    def clean(self):
        cleaned_data = super().clean()
        curso = cleaned_data.get('curso')

        # Verificar si el alumno ya está registrado en algún curso
        if Alumno.objects.filter(curso=curso).exists():
            self.add_error('curso', 'Ya estás inscrito en un curso. No puedes inscribirte en más de uno.')

        return cleaned_data

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if len(dni) != 8:
            raise forms.ValidationError("El DNI debe tener 8 caracteres.")
        return dni

    def clean_cuil(self):
        cuil = self.cleaned_data.get('cuil')
        if len(cuil) != 11:
            raise forms.ValidationError("El CUIL debe tener 11 caracteres.")
        return cuil
