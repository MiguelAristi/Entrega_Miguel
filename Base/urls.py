from django import views
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    #inicio
    path('', HomeView.as_view(), name='home'),
#login y registro
    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='base/logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),
#vistas de vehiculos
    path('listaAutomoviles/', AutomovilLista.as_view(), name='automoviles'),
    path('listaCamionetas/', CamionetaLista.as_view(), name='camionetas'),
    path('listaSuvs/', SuvlLista.as_view(), name='suvs'),
    path('listaBicicletas/', BicicletaLista.as_view(), name='bicicletas'),
    path('listaMotos/', MotoLista.as_view(), name='motos'),
    path('listaDeportivos/', DeportivoLista.as_view(), name='deportivos'),
    path('listaOtros/', OtroLista.as_view(), name='otros'),
#detalles
    path('automovilDetalle/<int:pk>/', AutomovilDetalle.as_view(), name='automovil'),
    path('camionetaDetalle/<int:pk>/', CamionetaDetalle.as_view(), name='camioneta'),
    path('suvDetalle/<int:pk>/', SuvDetalle.as_view(), name='suv'),
    path('deportivoDetalle/<int:pk>/', DeportivoDetalle.as_view(), name='deportivo'),
    path('motoDetalle/<int:pk>/', MotoDetalle.as_view(), name='moto'),
    path('bicicletaDetalle/<int:pk>/', BicicletaDetalle.as_view(), name='bicicleta'),
    path('otroDetalle/<int:pk>/', OtroDetalle.as_view(), name='otro'),
#edicion
    path('automovilEdicion/<int:pk>/', AutomovilUpdate.as_view(), name='automovil_editar'),
    path('camionetaEdicion/<int:pk>/', CamionetaUpdate.as_view(), name='camioneta_editar'),
    path('suvEdicion/<int:pk>/', SuvUpdate.as_view(), name='suv_editar'),
    path('deportivoEdicion/<int:pk>/', DeportivoUpdate.as_view(), name='deportivo_editar'),
    path('motoEdicion/<int:pk>/', MotoUpdate.as_view(), name='moto_editar'),
    path('bicicletaEdicion/<int:pk>/', BicicletaUpdate.as_view(), name='bicicleta_editar'),
    path('otroEdicion/<int:pk>/', OtroUpdate.as_view(), name='otro_editar'),
#eliminar
    path('automovilBorrado/<int:pk>/', AutomovilDelete.as_view(), name='automovil_eliminar'),
    path('camionetaBorrado/<int:pk>/', CamionetaDelete.as_view(), name='camioneta_eliminar'),
    path('suvBorrado/<int:pk>/', SuvDelete.as_view(), name='suv_eliminar'),
    path('deportivoBorrado/<int:pk>/', DeportivoDelete.as_view(), name='deportivo_eliminar'),
    path('motoBorrado/<int:pk>/', MotoDelete.as_view(), name='moto_eliminar'),
    path('bicicletaBorrado/<int:pk>/', BicicletaDelete.as_view(), name='bicicleta_eliminar'),
    path('otroBorrado/<int:pk>/', OtroDelete.as_view(), name='otro_eliminar'),
#nuevo instrumento
    path('vehiculoCreacion/', VehiculoCreacion.as_view(), name='nuevo'),
#comentarios
    path('automovilDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('camionetaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('suvDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('deportivoDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('bicicletaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('motoDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('otroDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
#about
    path('acercaDeMi/', views.about, name='acerca_de_mi'),
]
