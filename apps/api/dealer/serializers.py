from rest_framework import serializers

from apps.models import Dealer, DealerAddress
from apps.api.car.serializers import CarPriceListSerializer


class DealerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerAddress
        fields = '__all__'


class DealerListSerializer(serializers.ModelSerializer):
    car_prices = CarPriceListSerializer(read_only=True, many=True)
    address = DealerAddressSerializer()

    class Meta:
        model = Dealer
        fields = '__all__'


class DealerSerializer(serializers.ModelSerializer):
    address = DealerAddressSerializer()

    class Meta:
        model = Dealer
        fields = '__all__'


class DealerStatisticSerializer(serializers.ModelSerializer):
    avg_car_price = serializers.DecimalField(decimal_places=2, max_digits=7)

    class Meta:
        model = Dealer
        fields = '__all__'


