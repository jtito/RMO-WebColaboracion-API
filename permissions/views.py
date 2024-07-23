from rest_framework.viewsets import ModelViewSet
from .models import DetailPermission, Permission
from .serializers import (
    DetailPermisosSerializer,
    PermisionSerializer,
)


class DetailPermisoView(ModelViewSet):
    queryset = DetailPermission.objects.all()
    serializer_class = DetailPermisosSerializer
    http_method_names = ["get"]


class PermissionView(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermisionSerializer
    http_method_names = ["get"]
