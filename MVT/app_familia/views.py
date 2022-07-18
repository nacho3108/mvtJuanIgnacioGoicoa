from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app_familia.models import Familiar

def familiar(self, nombre, apellido, email, edad, anioNacimiento):
    familiar = Familiar(nombre=nombre, apellido = apellido,email = email, edad = edad, anioNacimiento = anioNacimiento)

    familiar.save()
    return HttpResponse(f"""
        <p>Nombre: {familiar.nombre} - Apellido: {familiar.apellido} - Email: {familiar.email} - Edad: {familiar.edad} - Anio Nacimiento: {familiar.anioNacimiento} agregado</p>
    """)

def familiares(self):

    lista = Familiar.objects.all()

    return render(self, "vistaFamiliar.html", {"vistaFamiliar": lista})

def listaFamilia(self):

    lista = Familiar.objects.all()

    return render(self, "listaFamiliar.html", {"famiiar": lista})    
