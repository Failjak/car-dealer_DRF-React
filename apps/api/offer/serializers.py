from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.registration.serializers import ProfileSerializer
from ..car.serializers import CarSerializer, CarPriceSerializer
from ..dealer.serializers import DealerSerializer
from apps.models import Offer


class OfferListSerializer(ModelSerializer):
    profile = ProfileSerializer()
    car = CarPriceSerializer()
    dealer = DealerSerializer()

    class Meta:
        model = Offer
        fields = '__all__'


class OfferSerializer(ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('car') not in attrs.get('dealer').car_prices.all():
            raise serializers.ValidationError({"car": "Does not belong to this dealer"})
        return attrs
