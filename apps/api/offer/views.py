from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin

from apps.models import Offer
from .serializers import OfferListSerializer


class OfferGetView(ListModelMixin,
                   RetrieveModelMixin,
                   CreateModelMixin,
                   GenericViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return OfferListSerializer
        OfferSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
