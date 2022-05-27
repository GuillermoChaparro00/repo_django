from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Personas
from django.template import loader
# Create your views here.
def verPersonas(request):
    lasper=Personas.objects.all()
    diccionario={"Personas": lasper}
    platilla=loader.get_template("verPersonas.html")
    documento=platilla.render(diccionario)
    return HttpResponse(documento)


def alta_Persona(request):
    persona= Personas(nombre="Nancy",apellido="Gerez",edad=47,dni=386374846, nacimiento="1997-12-11")
    persona.save()
    text= f"Persona:{persona.nombre} Edad:{persona.edad} se guardo en la BD"
    return HttpResponse(text)


def cargar_Persona(request):

    if request.method=="POST":
        persona= Personas(nombre= request.POST["nombre"],apellido="Chaparro",edad=26,dni=2387535)
        persona.save()
    return render(request, "cargarPersona.html")
