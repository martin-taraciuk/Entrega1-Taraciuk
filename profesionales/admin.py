from django.contrib import admin

from profesionales.models import Futbolista, Surfista, Tenista

# Register your models here.

admin.site.register(Surfista)
admin.site.register(Futbolista)
admin.site.register(Tenista)