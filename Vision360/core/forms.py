from django import forms
from .models import Carrera, Facultad, Bloque

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre', 'semestres', 'facultad', 'recorrido']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'semestres': forms.NumberInput(attrs={'class': 'form-control'}),
            'facultad': forms.Select(attrs={'class': 'form-control'}),
            'recorrido': forms.RadioSelect(choices=((True, 'Sí'), (False, 'No')), attrs={'class': 'form-check-input'})
        }


class FacultadForm(forms.ModelForm):
    class Meta:
        model = Facultad
        fields = ['nombre', 'siglas', 'ubicacion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'siglas': forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacion': forms.URLInput(attrs={'class': 'form-control'}),
        }


class BloqueForm(forms.ModelForm):
    class Meta:
        model = Bloque
        fields = ['codigo_identificativo','nombre', 'carrera', 'descripcion', 'estado', 'imagen', 'link']
        widgets = {
            'codigo_identificativo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'carrera': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control-file'}),
            'link': forms.URLInput(attrs={'class': 'form-control'})
        }

