from xml.parsers.expat import model
from django import forms

from profesionales import models

class SurfistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    pais = forms.CharField(max_length=30)
    
class FutbolistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    club_futbol = forms.CharField(max_length=50)
    
class TenistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    club_tenis = forms.CharField(max_length=50)
    
class SurfistaBusqueda(forms.Form):
    nombre = forms.CharField(max_length=20)