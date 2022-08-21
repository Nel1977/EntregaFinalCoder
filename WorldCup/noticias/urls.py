from django.urls import path
from noticias.views import (
    inicio, NoticiaList
)

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('lista-noticias/', NoticiaList.as_view(), name="ListaNoticias"),
]