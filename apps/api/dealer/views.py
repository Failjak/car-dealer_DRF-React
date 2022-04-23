from rest_framework.viewsets import ModelViewSet

from apps.models.dealership import Dealer, DealerAddress
from .serializers import DealerSerializer, DealerListSerializer, DealerAddressSerializer
from .filters import DealerFilter


class DealerViewSet(ModelViewSet):
    queryset = Dealer.objects.all()
    filterset_class = DealerFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return DealerListSerializer
        else:
            return DealerSerializer


class DealerAddressViewSet(ModelViewSet):
    queryset = DealerAddress.objects.all()
    serializer_class = DealerAddressSerializer
