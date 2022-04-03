from rest_framework.routers import SimpleRouter

from .views import OfferGetView


router = SimpleRouter()
router.register('', OfferGetView, basename='offer-get')

urlpatterns = router.urls
