from django.urls import path, include


urlpatterns = [
    path('car/', include('apps.api.car.urls')),
    path('dealer/', include('apps.api.dealer.urls')),
    path('offer/', include('apps.api.offer.urls')),
]
