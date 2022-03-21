from rest_framework.viewsets import ModelViewSet

from .serializers import CurrencySerializer
from apps.models import Currency


class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
