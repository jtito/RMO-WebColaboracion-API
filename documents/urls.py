from rest_framework.routers import DefaultRouter
from .views import (
    DocumentViewSet,
    PerfilxDocsViewSet,
    TypeDocumentViewSet,
    StateViewSet,
)

router = DefaultRouter()
router.register(r"docs", DocumentViewSet)
router.register(r"tipo", TypeDocumentViewSet)
router.register(r"perfil/user", PerfilxDocsViewSet)
router.register(r"state", StateViewSet)
urlpatterns = router.urls
