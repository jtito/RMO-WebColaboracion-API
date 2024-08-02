from rest_framework.routers import DefaultRouter
from .views import PerfilView, PerfilSimpleView

router = DefaultRouter()
router.register(r'perfil', PerfilView, basename='perfil')
router.register(r'simple', PerfilSimpleView, basename='simple')

urlpatterns = router.urls