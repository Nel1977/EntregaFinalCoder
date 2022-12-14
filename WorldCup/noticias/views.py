from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from noticias.models import Noticia

# Create your views here.

def inicio(self):
    return render(self, "inicio.html")

def sobre_mi(self):
    return render(self, "sobre-mi.html")

class NoticiaList(ListView):
    model = Noticia
    template_name = 'noticias.html'
    context_object_name = 'noticias'
    paginate_by = 3

class NoticiaDetail(DetailView):
    model = Noticia
    template_name = 'noticia.html'
    context_object_name = 'noticia'

@method_decorator(staff_member_required, name='dispatch')
class NoticiaCreate(CreateView):
    model = Noticia
    template_name = 'cargar-noticia.html'
    fields = ["titulo", "subtitulo", "contenido", "imagen", "fecha", "autor"]
    success_url = '/lista-noticias/'

@method_decorator(staff_member_required, name='dispatch')
class NoticiaUpdate(UpdateView):
    model = Noticia
    template_name = 'editar-noticia.html'
    fields = ('__all__')
    success_url = '/lista-noticias/'

@method_decorator(staff_member_required, name='dispatch')
class NoticiaDelete(DeleteView):
    model = Noticia
    template_name = 'eliminar-noticia.html'
    success_url = '/lista-noticias/'

def buscar_noticia(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.all()

    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda) |
            Q(subtitulo__icontains = busqueda) |
            Q(contenido__icontains = busqueda)
        ).distinct()
        return render(request, "resultado-busqueda.html", {"noticias": noticias})
    else:
        mensaje = "No se enviaron datos."
        return render(request, "resultado-busqueda.html", {"mensaje": mensaje})




