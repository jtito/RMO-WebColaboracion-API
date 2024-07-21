from rest_framework.viewsets import ModelViewSet
from .models import Role
from .serializers import (

    RoleGetSerializer,
    RolePostSerializer,
)

class RoleView(ModelViewSet):
    queryset = Role.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return RolePostSerializer
        return RoleGetSerializer
