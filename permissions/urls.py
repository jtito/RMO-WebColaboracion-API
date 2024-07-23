from rest_framework.routers import DefaultRouter
from .views import DetailPermisoView,PermissionView

router = DefaultRouter()
router.register(r"det-permission", DetailPermisoView, basename="detalle_permisos")
router.register(r"permiso",PermissionView, basename="permisos")


urlpatterns = router.urls