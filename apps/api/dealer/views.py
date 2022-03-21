from rest_framework.viewsets import ModelViewSet

from apps.models.dealership import Dealer, DealerAddress
from .serializers import DealerAddressSerializer, DealerSerializer


class DealerViewSet(ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class DealerAddressViewSet(ModelViewSet):
    queryset = DealerAddress.objects.all()
    serializer_class = DealerAddressSerializer
