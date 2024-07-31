from rest_framework.viewsets import ModelViewSet
from .models import Permission
from .serializers import PermisionSerializer


class PermissionView(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermisionSerializer
    http_method_names = ["get"]
