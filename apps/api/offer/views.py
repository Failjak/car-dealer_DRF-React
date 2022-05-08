from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from apps.models import Offer
from .serializers import OfferListSerializer, OfferSerializer
from .services import handle_user_offer
from apps.common.common import error_response_handler_decorator


class OfferGetView(ListModelMixin,
                   RetrieveModelMixin,
                   CreateModelMixin,
                   GenericViewSet):
    # TODO paginator
    # pagination_class =

    permission_classes = [IsAuthenticated, ]
    queryset = Offer.objects.order_by('-created_at').all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return OfferListSerializer
        return OfferSerializer

    def perform_create(self, serializer):
        return serializer.save()

    @error_response_handler_decorator
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        offer = self.perform_create(serializer)

        handle_user_offer(offer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return self.queryset
        return self.queryset.filter(profile__user=user)
