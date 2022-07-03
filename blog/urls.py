from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pages/<int:id>', views.pages, name='pages'),
    path('subir_post', views.Subir_post.as_view(), name='subir_post'),
    path('editar/<int:pk>', views.Editar_post.as_view(), name='editar_post'),
    path('eliminar/<int:pk>', views.Eliminar_post.as_view(), name='eliminar_post'),
    path('login', views.usuario_login, name='login'),
    path('logout', views.usuario_logout, name='logout'),
    path('registro', views.registro, name='registro')
]