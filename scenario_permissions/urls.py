from rest_framework.routers import DefaultRouter
from .views import DetailPermisoView

router = DefaultRouter()
router.register(r"escenario", DetailPermisoView, basename="detalle_permisos")


urlpatterns = router.urls