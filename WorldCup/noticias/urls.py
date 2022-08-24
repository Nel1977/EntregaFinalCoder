from django.urls import path
from noticias.views import (
    inicio, NoticiaList, NoticiaDetail, NoticiaCreate
)

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('lista-noticias/', NoticiaList.as_view(), name="ListaNoticias"),
    path('noticia/<int:pk>', NoticiaDetail.as_view(), name="Noticia"),
    path('cargar-noticia/', NoticiaCreate.as_view(), name="CargarNoticia"),
]