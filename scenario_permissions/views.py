from rest_framework.viewsets import ModelViewSet
from .models import DetailPermission
from .serializers import DetailPermisosSerializer


class DetailPermisoView(ModelViewSet):
    queryset = DetailPermission.objects.all()
    serializer_class = DetailPermisosSerializer
    http_method_names = ["get"]
