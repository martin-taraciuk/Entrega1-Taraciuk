from django.urls import path
from . import views

urlpatterns = [
    path('surfistas/', views.lista_surfistas, name="surfistas"),
    path('surfistas/crear/', views.crear_surfista, name="crear_surfista"),
    path('surfistas/<int:pk>', views.DetalleSurfista.as_view(), name="detalle_surfista"),
    path('surfistas/<int:pk>/editar', views.EditarSurfista.as_view(), name="editar_surfista"),
    path('surfistas/<int:pk>/borrar', views.BorrarSurfista.as_view(), name="borrar_surfista")

    
]
