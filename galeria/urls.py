from django.urls import path
from galeria import views

urlpatterns = [
    # Sesión
     path('', views.Bienvenida, name='bienvenida'),
     path('login', views.login_usuario, name='login'),
     path('logout', views.logout_usuario, name='logout'),
    # Registro
     path('registroUsuario', views.UsuarioCrear, name='registroUsuario'),
     path('registroGaleria', views.GaleriaCrear, name='registroGaleria'),
     path('registroFoto/<int:id_galeria>', views.FotoCrear, name='registroFoto'),
    # Listar
     path('listarUsuario', views.UsuarioListar, name="listarUsuario"),
     path('listarGaleria', views.GaleriaListar, name="listarGaleria"),
     path('listarFoto/<int:id_galeria>', views.FotoListar, name='listarFoto'),
    # Editar
     path('editarUsuario/<int:id_usuario>', views.UsuarioEditar, name='editarUsuario'),
     path('editarGaleria/<int:id_galeria>', views.GaleriaEditar, name='editarGaleria'),
     path('editarFoto/<int:id_foto>/<int:id_galeria>', views.FotoEditar, name='editarFoto'),
    # Miembros de galerias
     path('verMiembros/<int:id_galeria>', views.VerMiembros, name='verMiembros'),
     path('agregarMiembros/<int:id_galeria>/<int:id_usuario>', views.AgregarMiembro, name='agregarMiembros'),
     path('eliminarMiembro/<int:id_galeria>/<int:id_usuario>', views.EliminarMiembro, name='eliminarMiembro'),
]
