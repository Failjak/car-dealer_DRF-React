from rest_framework.routers import SimpleRouter

from .views import CarViewSet, CarPriceViewSet


router = SimpleRouter()
router.register('', CarViewSet, basename='car_car')
router.register('', CarPriceViewSet, basename='car_car_price')

urlpatterns = router.urls
