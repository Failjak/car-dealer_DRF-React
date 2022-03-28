from rest_framework import serializers

from apps.models import Car, CarPrice
from apps.api.wallets.serializers import CurrencySerializer


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPrice
        fields = '__all__'
