from rest_framework.routers import SimpleRouter

from .views import DealerViewSet, DealerAddressViewSet


router = SimpleRouter()
router.register('address', DealerAddressViewSet, basename='dealer_address')
router.register('', DealerViewSet, basename='dealer')

urlpatterns = router.urls
