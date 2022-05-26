from django.urls import path
from . import views

#format_filmu, cena, film, rodzaj
app_name = 'filmy'
urlpatterns = [
    path('',views.index, name='index'),
    path('rodzaj',views.rodzaj, name='rodzaj'),
    path('format_filmu',views.format_filmu, name='format_filmu'),
    path('film', views.film, name='film'),
    path('cena',views.cena, name='cena')
]

