from rest_framework import serializers

from apps.models import Car, CarPrice
from apps.api.wallets.serializers import CurrencySerializer


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarPriceSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer(read_only=True)
    car = CarSerializer(read_only=True)

    class Meta:
        model = CarPrice
        fields = '__all__'
