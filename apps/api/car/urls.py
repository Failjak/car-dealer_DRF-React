from rest_framework.routers import SimpleRouter

from .views import CarViewSet, CarPriceViewSet


router = SimpleRouter()
router.register('price', CarPriceViewSet, basename='car_price')
router.register('', CarViewSet, basename='car')

urlpatterns = router.urls
