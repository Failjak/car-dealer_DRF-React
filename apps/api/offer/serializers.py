from rest_framework.serializers import ModelSerializer

from apps.registration.serializers import UserSerializer
from apps.models import Offer


class OfferListSerializer(ModelSerializer):
    profile = ()

    class Meta:
        model = Offer
        fields = '__all__'

# class OfferSerializer(ModelSerializer):
#     class