from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('perfil/', views.perfil, name='perfil_usuario'),
    path('', views.inicio, name='index'),
    path('logout/', auth_views.LogoutView.as_view(next_page='iniciar_sesion'), name='logout'),


]
