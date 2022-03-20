from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, ListModelMixin, \
    DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.models.dealership import Dealer, DealerAddress
from .serializers import DealerAddressSerializer, DealerSerializer


class DealerViewSet(ListModelMixin,
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    CreateModelMixin,
                    DestroyModelMixin,
                    GenericViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class DealerAddressViewSet(ListModelMixin,
                           RetrieveModelMixin,
                           UpdateModelMixin,
                           CreateModelMixin,
                           DestroyModelMixin,
                           GenericViewSet):
    queryset = DealerAddress.objects.all()
    serializer_class = DealerAddressSerializer
