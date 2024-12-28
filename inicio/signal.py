from django.contrib.auth.models import Group
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

@receiver(user_signed_up)
def assign_alumno_group(sender, request, user, **kwargs):
    # Obtener el grupo "Alumno"
    alumno_group = Group.objects.get(name='Alumnos')
    
    # Asignar al usuario el grupo "Alumno"
    user.groups.add(alumno_group)
    user.save()
