from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
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


class RoleChoicesView(APIView):
    def get(self, request, *args, **kwargs):
        role_choices = Role.get_role_choies()
        formatted_choices = [
            {"value": value, "display_name": display_name}
            for value, display_name in role_choices
        ]
        return Response(formatted_choices)