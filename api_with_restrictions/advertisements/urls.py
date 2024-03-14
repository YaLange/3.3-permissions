from rest_framework.routers import DefaultRouter

from advertisements.views import AdvertisementViewSet, AdvertisementFavoritesViewSet

router = DefaultRouter()
router.register('advertisements', AdvertisementViewSet)
router.register('advertisements_favorites', AdvertisementFavoritesViewSet)

urlpatterns = router.urls
