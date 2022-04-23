from rest_framework import serializers

from apps.models import Car, CarPrice


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPrice
        fields = '__all__'


class CarPriceListSerializer(serializers.ModelSerializer):
    car = CarSerializer()

    class Meta:
        model = CarPrice
        fields = '__all__'
