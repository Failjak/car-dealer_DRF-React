from rest_framework import serializers

from apps.models import Dealer, DealerAddress
from apps.api.car.serializers import CarPriceSerializer


class DealerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerAddress
        fields = '__all__'


class DealerListSerializer(serializers.ModelSerializer):
    car_prices = CarPriceSerializer(read_only=True, many=True)
    address = DealerAddressSerializer()

    class Meta:
        model = Dealer
        fields = '__all__'


class DealerSerializer(serializers.ModelSerializer):
    address = DealerAddressSerializer()

    class Meta:
        model = Dealer
        fields = '__all__'


