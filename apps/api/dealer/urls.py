from rest_framework.routers import SimpleRouter

from .views import DealerViewSet, DealerAddressViewSet, DealerStatisticView


router = SimpleRouter()
# router.register('address', DealerAddressViewSet, basename='dealer_address')
router.register('statistic', DealerStatisticView, basename='dealer-statistic')
router.register('', DealerViewSet, basename='dealer')

urlpatterns = router.urls
