from django.contrib import admin

# Register your models here.

from .models import format_filmu, cena, film, rodzaj

admin.site.register(rodzaj)
admin.site.register(format_filmu)
admin.site.register(cena)
admin.site.register(film)