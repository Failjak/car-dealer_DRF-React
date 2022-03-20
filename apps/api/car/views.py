from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, ListModelMixin, \
    DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.models.car import Car, CarPrice
from .serializers import CarSerializer, CarPriceSerializer


class CarViewSet(ListModelMixin,
                 RetrieveModelMixin,
                 UpdateModelMixin,
                 CreateModelMixin,
                 DestroyModelMixin,
                 GenericViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarPriceViewSet(ListModelMixin,
                      RetrieveModelMixin,
                      UpdateModelMixin,
                      CreateModelMixin,
                      DestroyModelMixin,
                      GenericViewSet):
    queryset = CarPrice.objects.all()
    serializer_class = CarPriceSerializer
