from django.urls import path
from noticias.views import (
    inicio,
)

urlpatterns = [
    path('', inicio, name="Inicio"),
]