from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from .models import format_filmu, rodzaj, cena, film
from django.http import Http404
from webbrowser import get
from django.shortcuts import get_object_or_404, render
from multiprocessing import context


# Create your views here.

#format_filmu, rodzaj, cena, film


def index(request):
    index_list='film','rodzaj','cena','format_filmu'
    template=loader.get_template('filmy/index.html')
    context= {
        'index_list': index_list,
    }
    return HttpResponse(template.render(context, request))

def rodzajview(request):
    rodzaj_list=rodzaj.objects.all()
    template=loader.get_template('filmy/rodzaj.html')
    context= {
        'rodzaj_list': rodzaj_list,
    }
    return HttpResponse(template.render(context, request))

def filmview(request):
    film_list=film.objects.all()
    template=loader.get_template('filmy/film.html')
    context= {
        'film_list': film_list,
    }
    return HttpResponse(template.render(context, request))

def format_filmuview(request):
    format_filmu_list=format_filmu.objects.all()
    template=loader.get_template('filmy/format_filmu.html')
    context= {
        'format_filmu_list': format_filmu_list,
    }
    return HttpResponse(template.render(context, request))

def cenaview(request):
    cena_list=cena.objects.all()
    template=loader.get_template('filmy/cena.html')
    context= {
        'cena_list': cena_list,
    }
    return HttpResponse(template.render(context, request))


