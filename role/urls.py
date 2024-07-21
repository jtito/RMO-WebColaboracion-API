from rest_framework.routers import DefaultRouter
from .views import DetailPermisoDocsView,PermissionView,RoleView
router = DefaultRouter()
router.register(r"role", RoleView, basename="roles")

urlpatterns = router.urls