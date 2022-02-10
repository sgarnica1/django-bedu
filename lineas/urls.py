
from django.urls import path, include
from lineas import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('lineas', views.LineaView)
lineas_router = routers.NestedDefaultRouter(router, 'lineas', lookup='linea')
lineas_router.register('estaciones', views.LineaEstacionView,
                       basename="linea-estaciones")

router.register('estaciones', views.EstacionView)
router.register('viajes', views.ViajeView)
router.register('pasajero', views.PasajeroView)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(lineas_router.urls))
]
