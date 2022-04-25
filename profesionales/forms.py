from django import forms
from ckeditor.fields import RichTextFormField

class SurfistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    pais = forms.CharField(max_length=30)
    foto = forms.ImageField(required=False)
    tarjeta_presentacion = RichTextFormField(required=False)
    
    
class SurfistaBusqueda(forms.Form):
    nombre = forms.CharField(max_length=20)
    
