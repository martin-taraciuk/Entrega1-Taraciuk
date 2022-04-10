from django.shortcuts import redirect, render

from .models import Surfista, Futbolista, Tenista
from .forms import SurfistaFormulario, SurfistaBusqueda, FutbolistaFormulario, TenistaFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def crear_surfista(request):
    
    if request.method == 'POST':
        form = SurfistaFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            surfista = Surfista(nombre=data['nombre'], apellido=data['apellido'], pais=data['pais'])
            surfista.save()
            # return render(request, "index/plantilla.html", {})
            # return redirect('plantilla')
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
    fields = ['nombre', 'apellido', 'pais']
    
class BorrarSurfista(LoginRequiredMixin, DeleteView):    
    model = Surfista
    success_url = '/profesionales/surfistas/'

def crear_futbolista(request):
    
    if request.method == 'POST':
        form = FutbolistaFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            futbolista = Futbolista(nombre=data['nombre'], apellido=data['apellido'], club_futbol=data['club_futbol'])
            futbolista.save()
            # return render(request, "index/plantilla.html", {})
            # return redirect('plantilla')
            return redirect('index')
    
    form = FutbolistaFormulario()
    return render(request, "profesionales/crear_futbolista.html", {'form': form})

def crear_tenista(request):
    
    if request.method == 'POST':
        form = TenistaFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            tenista = Tenista(nombre=data['nombre'], apellido=data['apellido'], club_tenis=data['club_tenis'])
            tenista.save()
            # return render(request, "index/plantilla.html", {})
            # return redirect('plantilla')
            return redirect('index')
    
    form = TenistaFormulario()
    return render(request, "profesionales/crear_tenista.html", {'form': form})

