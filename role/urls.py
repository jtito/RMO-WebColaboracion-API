from rest_framework.routers import DefaultRouter
from .views import RoleView, RoleSimpleView
router = DefaultRouter()
router.register(r"role", RoleView, basename="roles")
router.register(r"simple",RoleSimpleView)


urlpatterns = router.urls