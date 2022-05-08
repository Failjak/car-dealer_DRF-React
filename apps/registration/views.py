from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.models import Profile
from .serializers import UserRegistrationSerializer, UserSerializer, ProfileGetSerializer, ProfileSerializer, ProfileCarSerializer
from apps.api.offer.serializers import ProfileOfferSerializer


class UserRegistration(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, balance = serializer.save()

        Profile.objects.create(user=user, balance=balance)

        return Response(
            {
                'user': UserSerializer(user).data,
                'message': 'User has been created successfully!'
            },
            status=status.HTTP_201_CREATED
        )


class ProfileGetView(ListModelMixin,
                     UpdateModelMixin,
                     RetrieveModelMixin,
                     GenericViewSet):
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ProfileGetSerializer
        return ProfileSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Profile.objects.all()
        return Profile.objects.filter(user=user)


class ProfileOfferGetView(ListModelMixin,
                          RetrieveModelMixin,
                          GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileOfferSerializer
    queryset = Profile.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Profile.objects.all()
        return Profile.objects.filter(user=user)


class ProfileCarGetView(ListModelMixin,
                        RetrieveModelMixin,
                        GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileCarSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Profile.objects.all()
        return Profile.objects.filter(user=user)
