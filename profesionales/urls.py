from django.urls import path
from . import views

urlpatterns = [
    path('surfista/crear/', views.crear_surfista, name="crear_surfista"),
    path('surfistas/', views.lista_surfistas, name="lista_surfistas"),
    path('futbolista/crear/', views.crear_futbolista, name="crear_futbolista"),
    path('tenista/crear/', views.crear_tenista, name="crear_tenista")
    
]
