from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    creada = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    editada = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ['-creada']

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    subtitulo = models.CharField(max_length=400, verbose_name="Subtítulo")
    contenido = models.TextField(verbose_name="Contenido")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="noticias")
    publicada = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    autor = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria, verbose_name="Categorías")
    creada = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    editada = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering = ['-creada']

    def __str__(self):
        return self.titulo

