import datetime

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
# Views
from django.views.generic import TemplateView, CreateView
# apps entradas
from applications.entrada.models import Entry
# Models 
from .models import Home
# Form
from .forms import SuscribersForm, ContactForm

class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)

        # Cargamos el home
        context["home"] = Home.objects.latest('created') # Traeme el ultimo en base a la fecha de creacion

        # Contexto de portada
        context["portada"] = Entry.objects.entrada_portada()

        # Contexto para los articulos en home
        context["entradas_home"] = Entry.objects.entradas_home()

        # Contexto para los articulos recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes()

        # Enviamos formulario de suscripcion
        context["form"] = SuscribersForm

        return context



class SuscribersCreateView(CreateView):
    form_class = SuscribersForm
    success_url = '.'

# Formulario para contacto que funciona en todos los templates
class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '.'

    