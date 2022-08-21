from django.urls import path
from noticias.views import (
    inicio, NoticiaList, NoticiaDetail
)

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('lista-noticias/', NoticiaList.as_view(), name="ListaNoticias"),
    path('noticia/<int:pk>', NoticiaDetail.as_view(), name="Noticia"),
]