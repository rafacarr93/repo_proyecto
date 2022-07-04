from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=datetime.now)
    imagen = models.ImageField(upload_to='imgs_posts', null=True, blank=True)

    def __str__(self):
        return self.titulo + ' - ' + str(self.autor)

    def get_absolute_url(self):
        return reverse('inicio')

    class Meta:
        ordering = ['-fecha']

class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.post.titulo + ' - ' + str(self.nombre) + ' - ' + str(self.cuerpo)