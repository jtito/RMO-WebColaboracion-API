from rest_framework.routers import DefaultRouter
from .views import UsuarioView

router = DefaultRouter()
router.register(r"usuarios", UsuarioView)

urlpatterns = router.urls