import graphene
from django import forms
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoFormMutation
from lineas import models


class LineaType(DjangoObjectType):
    class Meta:
        model = models.Linea
        fields = ['id', 'nombre', 'ubicacion', 'estaciones']


class LineaForm(forms.Form):
    nombre = forms.CharField()
    ubicacion = forms.CharField()


class LineaMutation(DjangoFormMutation):
    class Meta:
        form_class = LineaForm


class EstacionType(DjangoObjectType):
    class Meta:
        model = models.Estacion
        fields = ['id', 'nombre', 'linea',
                  'distancia_anterior', 'estacion_anterior']


class ViajeType(DjangoObjectType):
    class Meta:
        model = models.Viaje
        fields = ['estacion_entrada', 'hora_inicio',
                  'estacion_salida', 'hora_salida', 'pasajero']


class PasajeroType(DjangoObjectType):
    class Meta:
        model = models.Pasajero
        fields = ['nombre', 'apellido']


class PasajeroMutation(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        nombre = graphene.String(required=True)


class Query(graphene.ObjectType):
    lineas = graphene.List(LineaType)
    estaciones = graphene.List(EstacionType)
    viajes = graphene.List(ViajeType)
    pasajeros = graphene.List(PasajeroType)

    def resolve_lineas(root, info):
        return models.Linea.objects.all()

    def resolve_estaciones(root, info):
        return models.Estacion.objects.all()

    def resolve_viajes(root, info):
        return models.Viaje.objects.all()

    def resolve_pasajeros(root, info):
        return models.Pasajero.objects.all()


class Mutation(graphene.ObjectType):
    create_lineas = LineaMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
