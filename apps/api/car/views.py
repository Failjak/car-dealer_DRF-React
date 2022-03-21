from rest_framework.viewsets import ModelViewSet

from apps.models import Car, CarPrice
from .serializers import CarSerializer, CarPriceSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarPriceViewSet(ModelViewSet):
    queryset = CarPrice.objects.all()
    serializer_class = CarPriceSerializer
