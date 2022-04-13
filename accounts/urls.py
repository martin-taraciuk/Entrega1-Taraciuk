from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import editar_usuario, mi_login, registrarse, usuario_datos

urlpatterns = [
    path('login/', mi_login, name='login'),
    path('editar/', editar_usuario, name='editar_usuario'),
    path('datos/', usuario_datos, name='usuario_datos'),
    path('registrarse/', registrarse, name='registrarse'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout')
]
