from django.urls import path, include


urlpatterns = [
    path('car/', include('apps.api.car.urls')),
    path('currency/', include('apps.api.wallets.urls')),
    # path('user/', include('apps.api.user.urls')),
    path('dealer/', include('apps.api.dealer.urls')),
    # path('offer/', include('apps.api.offer.urls')),
]
