from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import generics, status

from .serializers import UserRegistrationSerializer, UserSerializer


class UserRegistration(generics.GenericAPIView):

    permission_classes = (AllowAny, )
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                'user': UserSerializer(user).data,
                'message': 'User has been created successfully!'
            },
            # headers=headers,
            status=status.HTTP_201_CREATED
        )
