from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'fecha', 'autor']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class':'form-control'}),
            'contenido': forms.Textarea(attrs={'class':'form-control'}),
        }