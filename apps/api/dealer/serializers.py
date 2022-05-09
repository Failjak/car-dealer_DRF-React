from rest_framework import serializers
from rest_framework_dataclasses.serializers import DataclassSerializer

from apps.models import Dealer, DealerAddress
from apps.api.car.serializers import CarPriceListSerializer, CarSerializer
from apps.report.dataclasses import DealerStatistic


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


class DealerStatisticDTOSerializer(DataclassSerializer):
    most_popular_car = CarSerializer()
    address = DealerAddressSerializer()

    class Meta:
        dataclass = DealerStatistic
