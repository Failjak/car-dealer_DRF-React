from django.urls import path, include


urlpatterns = [
    path('auth/', include('apps.registration.urls')),
    path('', include('apps.api.urls')),
]
