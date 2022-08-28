from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mensaje(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['creado']

class Hilo(models.Model):
    usuarios = models.ManyToManyField(User, related_name='hilos')
    mensajes = models.ManyToManyField(Mensaje)

