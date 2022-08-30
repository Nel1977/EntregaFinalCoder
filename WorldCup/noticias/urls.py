from django.urls import path
from noticias.views import (
    inicio, sobre_mi, NoticiaList, NoticiaDetail, NoticiaCreate, NoticiaUpdate, NoticiaDelete, buscar_noticia
)

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('sobre-mi/', sobre_mi, name="SobreMi"),
    path('lista-noticias/', NoticiaList.as_view(), name="ListaNoticias"),
    path('noticia/<int:pk>', NoticiaDetail.as_view(), name="Noticia"),
    path('cargar-noticia/', NoticiaCreate.as_view(), name="CargarNoticia"),
    path('editar-noticia/<int:pk>', NoticiaUpdate.as_view(), name="EditarNoticia"),
    path('eliminar-noticia/<int:pk>', NoticiaDelete.as_view(), name="EliminarNoticia"),
    path('buscar-noticia/', buscar_noticia, name="BuscarNoticias"),
]