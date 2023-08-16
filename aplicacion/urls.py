from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home" ),
    path('servicios/', servicios, name="servicios" ),
    path('vehiculos/', vehiculos, name="vehiculos" ),
    path('productos/', productos, name="productos" ),
    path('agregarServicio/', agregarServicio, name="agregarServicio" ),
    path('agregarVehiculo/', agregarVehiculo, name="agregarVehiculo" ),
    path('agregarProducto/', agregarProducto, name="agregarProducto" ),
]