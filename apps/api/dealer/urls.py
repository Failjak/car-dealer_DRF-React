from rest_framework.routers import SimpleRouter

from .views import DealerViewSet, DealerAddressViewSet, DealerStatisticView


router = SimpleRouter()
# router.register('address', DealerAddressViewSet, basename='dealer_address')
router.register('', DealerViewSet, basename='dealer')
router.register('statistic', DealerStatisticView, basename='dealer-statistic')

urlpatterns = router.urls
