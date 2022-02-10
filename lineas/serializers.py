from .models import Linea, Estacion, Viaje, Pasajero
from rest_framework import serializers


class LineaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Linea
        fields = ['nombre', 'ubicacion']


class EstacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estacion
        fields = ['nombre', 'linea', 'distancia_anterior', 'estacion_anterior']


class ViajeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Viaje
        fields = ['estacion_entrada', 'hora_inicio',
                  'estacion_salida', 'hora_salida', 'pasajero']


class PasajeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pasajero
        fields = ['nombre', 'apellido']
