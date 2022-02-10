from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import LineaSerializer, EstacionSerializer, ViajeSerializer, PasajeroSerializer
from .models import Linea, Estacion, Viaje, Pasajero

# Create your views here.


class LineaView(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Linea.objects.all().order_by('id')
    serializer_class = LineaSerializer


class EstacionView(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Estacion.objects.all().order_by('id')
    serializer_class = EstacionSerializer


class LineaEstacionView(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = EstacionSerializer

    def get_queryset(self):
        return Estacion.objects.filter(linea=self.kwargs['linea_pk'])


class ViajeView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Viaje.objects.all().order_by('id')
    serializer_class = ViajeSerializer


class PasajeroView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Pasajero.objects.all().order_by('id')
    serializer_class = PasajeroSerializer
