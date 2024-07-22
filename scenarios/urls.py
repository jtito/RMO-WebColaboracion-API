from rest_framework.routers import DefaultRouter
from .views import ScenarioViewSet
router = DefaultRouter()
router.register(r'escenario',ScenarioViewSet)

urlpatterns = router.urls