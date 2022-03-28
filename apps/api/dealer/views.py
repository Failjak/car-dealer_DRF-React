from rest_framework.viewsets import ModelViewSet

from apps.models.dealership import Dealer, DealerAddress
from .serializers import DealerAddressSerializer, DealerSerializer, DealerListSerializer


class DealerViewSet(ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return DealerListSerializer
        elif self.action == 'create':
            return DealerSerializer


class DealerAddressViewSet(ModelViewSet):
    queryset = DealerAddress.objects.all()
    serializer_class = DealerAddressSerializer
