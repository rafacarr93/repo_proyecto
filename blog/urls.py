from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pages/<int:id>', views.pages, name='pages'),
    path('subir_post', views.Subir_post.as_view(), name='subir_post'),
    path('editar/<int:pk>', views.Editar_post.as_view(), name='editar_post'),
    path('eliminar/<int:pk>', views.Eliminar_post.as_view(), name='eliminar_post'),
    path('editar_perfil', views.Editar_usuario.as_view(), name='editar_perfil'),
    path('password/', views.Cambiar_password.as_view(template_name='cambiar_contraseña.html')),
    path('login', views.usuario_login, name='login'),
    path('logout', views.usuario_logout, name='logout'),
    path('registro', views.registro, name='registro'),
    path('pages/<int:pk>/comentar', views.Agregar_comentario.as_view(), name='comentar')
]