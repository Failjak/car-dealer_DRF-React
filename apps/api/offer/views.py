from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin

from apps.models import Offer, Profile
from .serializers import OfferListSerializer, OfferSerializer


class OfferGetView(ListModelMixin,
                   RetrieveModelMixin,
                   CreateModelMixin,
                   GenericViewSet):
    queryset = Offer.objects.order_by('-created_at').all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return OfferListSerializer
        return OfferSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # TODO offer logic
        # user =

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
