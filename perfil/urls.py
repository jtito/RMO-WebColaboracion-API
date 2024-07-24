from rest_framework.routers import DefaultRouter
from .views import PerfilView, PerfilSimpleView

router = DefaultRouter()
router.register(r"perfil", PerfilView, basename="perfiles")
router.register(r"simple",PerfilSimpleView)


urlpatterns = router.urls