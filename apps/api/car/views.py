from rest_framework.viewsets import ModelViewSet

from apps.models import Car, CarPrice
from .serializers import CarSerializer, CarPriceSerializer, CarPriceListSerializer
from .filters import CarPriceFilter


class CarViewSet(ModelViewSet):
    # TODO permission
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarPriceViewSet(ModelViewSet):
    # TODO permission
    queryset = CarPrice.objects.all()
    serializer_class = CarPriceSerializer
    filterset_class = CarPriceFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return CarPriceListSerializer
        return CarPriceSerializer
