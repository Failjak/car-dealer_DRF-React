from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.registration.serializers import ProfileSerializer
from ..car.serializers import CarPriceSerializer, CarSerializer
from ..dealer.serializers import DealerSerializer
from apps.models import Offer, Profile


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
        read_only_fields = ('status', )

    def validate(self, attrs):
        if attrs.get('car') not in attrs.get('dealer').car_prices.all():
            raise serializers.ValidationError({"car": "Does not belong to this dealer"})
        return attrs


class OfferToProfileSerializer(serializers.ModelSerializer):
    car = CarSerializer(source='car.car')

    dealer__id = serializers.SerializerMethodField()
    dealer__name = serializers.SerializerMethodField()

    def get_dealer__id(self, offer):
        return offer.dealer.id

    def get_dealer__name(self, offer):
        return offer.dealer.name

    class Meta:
        model = Offer
        fields = (
            'status',
            'dealer__id',
            'dealer__name',
            'car',
            'created_at',
            'updated_at',
        )


class ProfileOfferSerializer(serializers.ModelSerializer):
    profile_id = serializers.CharField(source='id')
    offers = serializers.SerializerMethodField()

    def get_offers(self, profile):
        offers = Offer.get_users_offers(profile)
        serializer = OfferToProfileSerializer(offers, many=True, read_only=True)
        return serializer.data

    class Meta:
        model = Profile
        fields = ('profile_id', 'offers')
