from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import format_filmu, rodzaj, cena, film
from django.http import Http404
from webbrowser import get
from django.shortcuts import get_object_or_404, render

# Create your views here.

#format_filmu, rodzaj, cena, film

#viewsy do zmiany, templates tez

def index(request):
    index_list='format_filmu',#'rodzaj','cena','film'
    template=loader.get_template('filmy/index.html')
    context= {
        'index_list': index_list,
    }
    return HttpResponse(template.render(context,request))

def rodzaj(request):
    rodzaj_list=rodzaj.objects.all
    template=loader.get_template('filmy/rodzaj.html')
    context= {
        'rodzaj_list': rodzaj_list,
    }
    return HttpResponse(template.render(context,request))

def film(request):
    film_list=film.objects.all
    template=loader.get_template('filmy/film.html')
    context= {
        'film_list': film_list,
    }
    return HttpResponse(template.render(context,request))

def format_filmu(request):
    format_filmu_list=format_filmu.objects.all
    template=loader.get_template('filmy/format_filmu.html')
    context= {
        'format_filmu_list': format_filmu_list,
    }
    return HttpResponse(template.render(context,request))

def cena(request):
    cena_list=cena.objects.all
    template=loader.get_template('filmy/cena.html')
    context= {
        'cena_list': cena_list,
    }
    return HttpResponse(template.render(context,request))



