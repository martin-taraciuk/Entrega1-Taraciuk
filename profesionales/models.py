from django.db import models

# Create your models here.

class Surfista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    folleto = models.CharField(max_length=500, null=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Futbolista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    club_futbol = models.CharField(max_length=50)
    
class Tenista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    club_tenis = models.CharField(max_length=50)