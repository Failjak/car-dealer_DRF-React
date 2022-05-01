from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from apps.models.dealership import Dealer, DealerAddress
from .serializers import DealerSerializer, DealerListSerializer, DealerAddressSerializer, DealerStatisticSerializer
from .filters import DealerFilter


class DealerViewSet(ModelViewSet):
    queryset = Dealer.objects.all()
    filterset_class = DealerFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return DealerListSerializer
        return DealerSerializer


class DealerAddressViewSet(ModelViewSet):
    queryset = DealerAddress.objects.all()
    serializer_class = DealerAddressSerializer


class DealerStatisticView(GenericViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerStatisticSerializer

    # TODO get most popular car

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
