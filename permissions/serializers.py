from rest_framework.serializers import ModelSerializer
from .models import DetailPermissionDocs, Permission
from scenarios.serializers import ScenarioSerializer


class PermisionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class DetailPermisosSerializer(ModelSerializer):
    escenario_id = ScenarioSerializer()
    permission_id = PermisionSerializer()

    class Meta:
        model = DetailPermissionDocs
        fields = "__all__"