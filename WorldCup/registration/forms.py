from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'nombre', 'apellido', 'email']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'nombre': forms.TextInput(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Nombre'}),
            'apellido': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Apellido'}),
            'email': forms.EmailInput(attrs={'class':'form-control mt-3', 'placeholder':'Email'}),
        }