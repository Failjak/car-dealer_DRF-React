from rest_framework import serializers
from django.contrib.auth.models import User

from apps.models import Profile


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
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
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('cars', 'balance')
