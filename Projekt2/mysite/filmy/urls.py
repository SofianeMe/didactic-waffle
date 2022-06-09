from django.urls import path
from . import views


#format_filmu, cena, film, rodzaj

app_name = 'filmy'
urlpatterns = [
    path('',views.index, name='index'),
    path('rodzaj/',views.rodzajview, name='rodzaj'),
    path('format_filmu/',views.format_filmuview, name='format_filmu'),
    path('film/', views.filmview, name='film'),
    path('cena/',views.cenaview, name='cena'),
]

