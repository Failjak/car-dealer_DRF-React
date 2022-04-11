from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.registration.serializers import ProfileSerializer
from ..car.serializers import CarSerializer
from ..dealer.serializers import DealerSerializer
from apps.models import Offer


class OfferListSerializer(ModelSerializer):
    profile = ProfileSerializer()
    car = CarSerializer()
    dealer = DealerSerializer()

    class Meta:
        model = Offer
        fields = '__all__'


class OfferSerializer(ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

    def validate(self, attrs):
        dealer_cars = [cp.car for cp in attrs['dealer'].car_prices.all()]
        if attrs['car'] not in dealer_cars:
            raise serializers.ValidationError({"car": "Does not belong to this dealer"})
        return attrs
