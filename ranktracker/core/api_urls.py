from rest_framework.routers import DefaultRouter
from .api_views import ClientViewSet, KeywordViewSet, RankResultViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'keywords', KeywordViewSet)
router.register(r'rankresults', RankResultViewSet)

urlpatterns = router.urls