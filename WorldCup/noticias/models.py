from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Noticia(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    subtitulo = models.CharField(max_length=400, verbose_name="Subtítulo")
    contenido = RichTextField()
    # contenido = models.TextField(verbose_name="Contenido")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="noticias")
    fecha = models.DateTimeField(verbose_name="Fecha", default=now)
    autor = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo

