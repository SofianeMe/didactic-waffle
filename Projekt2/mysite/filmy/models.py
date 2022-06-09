from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class format_filmu(models.Model):
    format = models.CharField(max_length=100)
    def __str__(self):
        return self.format

class rodzaj(models.Model):
    rodzaj_format = models.CharField(max_length=100)
    def __str__(self):
        return self.rodzaj_format

class cena(models.Model):
    cena_format = models.CharField(max_length=100)
    def __str__(self):
        return self.cena_format

class film(models.Model):
    format=models.ManyToManyField('format_filmu', 'rodzaj', 'cena')
    rodzaj=models.ForeignKey(rodzaj, on_delete=models.CASCADE)
    cena=models.ForeignKey(cena, on_delete=models.CASCADE)
    def __str__(self):
        return '{} - {} '.format(self.rodzaj, self.cena) 