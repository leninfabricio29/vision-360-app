from django.contrib import admin
from .models import Facultad,Bloque, Carrera
# Register your models here.

admin.site.register(Facultad)
admin.site.register(Carrera)
admin.site.register(Bloque)

