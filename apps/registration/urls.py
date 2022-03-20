from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserRegistration

"""
Сделана регистрация, надо сделать рассылку на почту. Так же полчения токена и 
авторизация сразу после регистрации.

Подключить селари для рассылки на почту.
"""

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistration.as_view(), name='register')
]
