from rest_framework.routers import DefaultRouter
from .views import PermissionView

router = DefaultRouter()
router.register(r"permiso",PermissionView, basename="permisos")


urlpatterns = router.urls