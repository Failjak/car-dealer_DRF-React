from rest_framework.routers import SimpleRouter

from .views import CurrencyViewSet


router = SimpleRouter()
router.register('', CurrencyViewSet, basename='currency_view')

urlpatterns = router.urls
