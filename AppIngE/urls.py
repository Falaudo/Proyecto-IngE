from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns= [
    path('', ListaPosts.as_view(), name = 'home'),
    path('about/',about, name='about'),
    path('registro/',register, name='registro'),
    path('ingresar/', login_request, name= 'ingresar' ),
    path('cerrarSesion/', logout_request, name='cerrarSesion' ),
    path('perfil/', perfil, name= 'perfil'),
    path('editarPerfil/', editarPerfil, name='editarPerfil' ),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
    path('posteos/', CrearPosteos.as_view(), name='posteos'),
    path('detallePost/<slug:slug>/', DetallePosts.as_view(), name = 'detallePost'),
    path('actualizarPost/<slug:slug>/', ActualizarPosteos.as_view(), name = 'actualizarPost'),
    path('borrarPost/<slug:slug>/', BorrarPosteos.as_view(), name = 'borrarPost'),
]

