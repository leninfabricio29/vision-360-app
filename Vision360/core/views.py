from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.template.loader import get_template
from django.views.generic import DetailView, View
from datetime import date
from django.contrib import messages
from .models import Facultad, Carrera, Bloque
from .forms import CarreraForm, FacultadForm, BloqueForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import permission_required

 


def homeView (request):
    user = request.user
    carreras = Carrera.objects.filter(recorrido=True).distinct()
    
    if user.is_superuser:
        contexto = {
            'user': user,
            }
        return render(request, "RestaurantBooking/PageUtils/home-admin.html", contexto)
    else:
        contexto = {
            'carreras': carreras
            }
        return render(request, "RestaurantBooking/PageUtils/home-user.html", contexto)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('page-home')
        else:
            error_message = 'Existe un error las con crendenciales.'
            return render(request, 'RestaurantBooking/PageUtils/login.html', {'error_message': error_message})
    else:
        return render(request, 'RestaurantBooking/PageUtils/login.html')

def logout_view(request):
    logout(request)
    # Redirecciona a la página de inicio o a donde desees después de cerrar sesión
    return redirect('page-login')

@permission_required('auth.is_superuser')
def lista_facultades(request):
    facultades = Facultad.objects.all()
    return render(request, 'RestaurantBooking/PagesFacultades/facultades.html', {'facultades': facultades})

@permission_required('auth.is_superuser')
def registrar_facultad(request):
    if request.method == 'POST':
        form = FacultadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page-facultades')  # Reemplaza 'nombre_de_la_url' con el nombre de la URL de la página de inicio
    else:
        form = FacultadForm()
    return render(request, 'RestaurantBooking/PagesFacultades/nueva-facultad.html', {'form': form})

@permission_required('auth.is_superuser')
def lista_carreras(request):
    carreras = Carrera.objects.all()
    return render(request, 'RestaurantBooking/PagesFacultades/carreras.html', {'carreras': carreras})

@permission_required('auth.is_superuser')
def registrar_carrera(request):
    if request.method == 'POST':
        form = CarreraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page-carreras')  # Reemplaza 'nombre_de_la_url' con el nombre de la URL de la página de inicio
    else:
        form = CarreraForm()
    return render(request, 'RestaurantBooking/PagesFacultades/nueva-carrera.html', {'form': form})

@permission_required('auth.is_superuser')
def listar_bloques(request):
    bloques = Bloque.objects.all()
    return render(request, 'RestaurantBooking/PagesFacultades/bloques.html', {'bloques': bloques})

@permission_required('auth.is_superuser')
def registrar_bloque(request):
    if request.method == 'POST':
        form = BloqueForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('page-bloques')  # Redirige a la página de lista de bloques
    else:
        form = BloqueForm()
    return render(request, 'RestaurantBooking/PagesFacultades/nuevo-bloque.html', {'form': form})


def bloques_carrera(request, carrera_id):
    # Obtener la carrera específica o devolver un error 404 si no existe
    carrera = get_object_or_404(Carrera, id=carrera_id)
    carreras = Carrera.objects.filter(recorrido=True).distinct()
    
    # Filtrar los bloques asociados a la carrera
    bloques = Bloque.objects.filter(carrera=carrera)
    
    contexto = {
        'carrera': carrera,
        'bloques': bloques,
        'carreras': carreras
    }
    return render(request, "RestaurantBooking/PagesFacultades/bloques-carrera.html", contexto)