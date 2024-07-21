from rest_framework.routers import DefaultRouter
from .views import DetailPermisoDocsView,PermissionView

router = DefaultRouter()
router.register(r"det-permission", DetailPermisoDocsView, basename="detalle_permisos")
router.register(r"permiso",PermissionView, basename="permisos")


urlpatterns = router.urls