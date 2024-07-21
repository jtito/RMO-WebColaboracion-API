from rest_framework.viewsets import ModelViewSet
from .models import DetailPermissionDocs, Permission
from .serializers import (
    DetailPermisosSerializer,
    PermisionSerializer,
)


class DetailPermisoDocsView(ModelViewSet):
    queryset = DetailPermissionDocs.objects.all()
    serializer_class = DetailPermisosSerializer
    http_method_names = ["get"]


class PermissionView(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermisionSerializer
    http_method_names = ["get"]
