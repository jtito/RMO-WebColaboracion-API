from rest_framework.viewsets import ModelViewSet
from .models import Role
from .serializers import RoleSerializer, RoleSimpleSerializer

class RoleView(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    http_method_names = ['get']

class RoleSimpleView(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSimpleSerializer
    http_method_names = ['get']