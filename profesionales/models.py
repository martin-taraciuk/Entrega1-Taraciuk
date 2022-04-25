from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


class Surfista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    tarjeta_presentacion = RichTextField(blank=True, null=True)
    foto = models.ImageField(upload_to='avatar',blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
