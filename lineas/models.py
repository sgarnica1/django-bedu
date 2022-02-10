from django.db import models

# Create your models here.


class Linea(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Estacion(models.Model):
    nombre = models.CharField(max_length=255)
    linea = models.ForeignKey(
        Linea, on_delete=models.CASCADE, related_name='estaciones')
    distancia_anterior = models.FloatField(default=0)
    estacion_anterior = models.OneToOneField(
        'self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Pasajero(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Viaje(models.Model):
    estacion_entrada = models.ForeignKey(
        Estacion, on_delete=models.SET_NULL, null=True, blank=False, related_name="entradas")
    hora_inicio = models.DateTimeField()
    estacion_salida = models.ForeignKey(
        Estacion, on_delete=models.SET_NULL, null=True, blank=False, related_name="salidas")
    hora_salida = models.DateTimeField()
    pasajero = models.ForeignKey(
        Pasajero, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return f'{self.estacion_entrada} {self.hora_inicio} - {self.pasajero}'
