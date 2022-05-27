from django import views
from django.urls import URLPattern
from django.urls import path
from . import views

urlpatterns=[
    path("verPersonas",views.verPersonas),
    path("alta_Persona",views.alta_Persona),
    path("cargar_Persona",views.cargar_Persona)

    
]