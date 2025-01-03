# Generated by Django 5.1.4 on 2024-12-28 18:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('matricula_maxima', models.PositiveIntegerField()),
                ('lugar', models.CharField(choices=[('Sede', 'Sede'), ('Subsede', 'Subsede'), ('Anexo', 'Anexo')], default='Sede', max_length=50)),
                ('proyecto', models.FileField(blank=True, null=True, upload_to='proyectos/')),
                ('directivo', models.ForeignKey(limit_choices_to={'groups__name': 'Directivo'}, on_delete=django.db.models.deletion.CASCADE, related_name='cursos_directivos', to=settings.AUTH_USER_MODEL)),
                ('instructor', models.ForeignKey(limit_choices_to={'groups__name': 'Instructor'}, on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inscripcion', models.DateField(auto_now_add=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscripciones', to='inicio.curso')),
                ('estudiante', models.ForeignKey(limit_choices_to={'groups__name': 'Alumno'}, on_delete=django.db.models.deletion.CASCADE, related_name='inscripciones', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('horas', models.PositiveIntegerField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modulos', to='inicio.curso')),
            ],
        ),
    ]
