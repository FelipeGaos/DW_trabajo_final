from django.urls import path
from galeria import views

urlpatterns = [
    # Sesión
     path('', views.Bienvenida, name='bienvenida'),
     path('login', views.login_usuario, name='login'),
     path('logout', views.logout_usuario, name='logout'),
     path('menuAdmin', views.MenuAdmin, name='menuAdmin'),
    # Registro
     path('registroUsuario', views.UsuarioCrear, name='registroUsuario'),
     path('registroUsuario_admin', views.UsuarioCrear_admin, name='registroUsuario_admin'),
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
    # Eliminar
     path('eliminarUsuario/<int:id_usuario>', views.UsuarioEliminar, name='eliminarUsuario'),
     path('eliminarGaleria/<int:id_galeria>', views.GaleriaEliminar, name='eliminarGaleria'),
     path('eliminarFoto/<int:id_foto>/<int:id_galeria>', views.FotoEliminar, name='eliminarFoto'),
    # Miembros de galerias
     path('verMiembros/<int:id_galeria>', views.VerMiembros, name='verMiembros'),
     path('agregarMiembros/<int:id_galeria>/<int:id_usuario>', views.AgregarMiembro, name='agregarMiembros'),
     path('eliminarMiembro/<int:id_galeria>/<int:id_usuario>', views.EliminarMiembro, name='eliminarMiembro'),
]
