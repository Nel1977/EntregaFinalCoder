from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from noticias.models import Noticia

# Create your views here.

def inicio(self):
    return render(self, "inicio.html")

class NoticiaList(ListView):
    model = Noticia
    template_name = 'noticias.html'
    context_object_name = 'noticias'
    paginate_by = 3

class NoticiaDetail(DetailView):
    model = Noticia
    template_name = 'noticia.html'
    context_object_name = 'noticia'

class NoticiaCreate(CreateView):
    model = Noticia
    template_name = 'cargar-noticia.html'
    fields = ["titulo", "subtitulo", "contenido", "imagen", "fecha", "autor"]
    success_url = '/lista-noticias/'




