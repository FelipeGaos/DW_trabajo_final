from django.urls import path
from galeria import views

urlpatterns = [
     path('registroUsuario', views.UsuarioCrear, name='registroUsuario'),
     path('registroGaleria', views.GaleriaCrear, name='registroGaleria'),
     path('registroFoto/<int:id_galeria>', views.FotoCrear, name='registroFoto'),
]
