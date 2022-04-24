from django.urls import path
from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserRegistration, ProfileGetView, ProfileOfferGetView, ProfileCarGetView

"""
Сделана регистрация, надо сделать рассылку на почту. Так же полчения токена и 
авторизация сразу после регистрации.

Подключить селари для рассылки на почту.
"""

router = SimpleRouter()
router.register('profile/offer', ProfileOfferGetView, basename='profile-offers_view')
router.register('profile/car', ProfileCarGetView, basename='profile-cars_view')
router.register('profile', ProfileGetView, basename='profile_view')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistration.as_view(), name='register'),
]

urlpatterns += router.urls

