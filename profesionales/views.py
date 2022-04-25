from django.shortcuts import redirect, render

from .models import Surfista
from .forms import SurfistaFormulario, SurfistaBusqueda
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def crear_surfista(request):
    
    if request.method == 'POST':
        form = SurfistaFormulario(request.POST, request.FILES)
        
        if form.is_valid():
            data = form.cleaned_data
            surfista = Surfista(nombre=data['nombre'], apellido=data['apellido'], pais=data['pais'], tarjeta_presentacion=data['tarjeta_presentacion'], foto=data['foto'])
            surfista.save()
            return redirect('index')
    
    form = SurfistaFormulario()
    return render(request, "profesionales/crear_surfista.html", {'form': form})

def lista_surfistas(request):
    
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar is not None:
        surfistas = Surfista.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        surfistas = Surfista.objects.all()
        
    form = SurfistaBusqueda()
    return render(request, "profesionales/lista_surfistas.html", {'form': form, 'surfistas': surfistas})

class DetalleSurfista(DetailView):
    model = Surfista
    template_name = "profesionales/detalle_surfista.html"

    
class EditarSurfista(LoginRequiredMixin, UpdateView):
    model = Surfista
    success_url = '/profesionales/surfistas/'
    fields = ['nombre', 'apellido', 'pais', 'tarjeta_presentacion', 'foto']
    
class BorrarSurfista(LoginRequiredMixin, DeleteView):    
    model = Surfista
    success_url = '/profesionales/surfistas/'



