from django.contrib import admin
from lineas.models import Linea, Estacion, Viaje, Pasajero

# Register your models here.


admin.site.register(Linea)
admin.site.register(Estacion)
admin.site.register(Viaje)
admin.site.register(Pasajero)
