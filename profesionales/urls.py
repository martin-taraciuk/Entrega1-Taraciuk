from django.urls import path
from . import views

urlpatterns = [
    path('surfistas/', views.lista_surfistas, name="surfistas"),
    path('surfistas/crear/', views.crear_surfista, name="crear_surfista"),
    path('surfistas/<int:pk>', views.DetalleSurfista.as_view(), name="detalle_surfista"),
    path('surfistas/<int:pk>/editar', views.EditarSurfista.as_view(), name="editar_surfista"),
    path('surfistas/<int:pk>/borrar', views.BorrarSurfista.as_view(), name="borrar_surfista"),
    # path('surfista/borrar/', views.borrar_surfista, name="borrar_surfista"),
    # path('surfista/actualizar/', views.actualizar_surfista, name="actulizar_surfista"),
    path('futbolista/crear/', views.crear_futbolista, name="crear_futbolista"),
    path('tenista/crear/', views.crear_tenista, name="crear_tenista")
    
]
