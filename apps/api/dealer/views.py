from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from apps.models.dealership import Dealer, DealerAddress
from .serializers import DealerSerializer, DealerListSerializer, DealerAddressSerializer, DealerStatisticDTOSerializer
from .filters import DealerFilter
from apps.report.dealer_report import get_dealer_statistic, get_dealers_statistic


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


class DealerStatisticView(ViewSet):
    def list(self, request, *args, **kwargs):
        queryset = Dealer.objects.all()
        stats = get_dealers_statistic(queryset)
        serializer = DealerStatisticDTOSerializer(stats, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Dealer.objects.all()
        dealer = get_object_or_404(queryset, pk=pk)
        dealer_stat = get_dealer_statistic(dealer)
        serializer = DealerStatisticDTOSerializer(dealer_stat)
        return Response(serializer.data)
