from rest_framework import serializers
from django.contrib.auth.models import User

from apps.models import Profile, Offer
from apps.api.car.serializers import CarPriceOfferSerializer


class UserRegistrationSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(source='user.profile.balance', max_digits=7, decimal_places=2)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "balance"
        )

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_date):
        user = User.objects.create_user(
            username=validated_date['username'],
            password=validated_date['password'],
            first_name=validated_date['first_name'],
            last_name=validated_date['last_name'],
        )
        return user, validated_date.get('user').get('profile').get('balance')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = (
            'last_login',
            'password',
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'groups',
            'user_permissions'
        )


class ProfileSerializer(serializers.ModelSerializer):
    user = UserUpdateSerializer()

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('cars', 'balance')


class ProfileGetSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCarSerializer(serializers.ModelSerializer):
    profile_id = serializers.CharField(source='id')
    cars = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('profile_id', 'cars')

    def get_cars(self, profile):
        cars = Offer.get_users_cars(profile)
        ser = CarPriceOfferSerializer([car for car in cars], many=True, read_only=True)
        return ser.data
