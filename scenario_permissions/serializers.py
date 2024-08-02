from rest_framework.serializers import ModelSerializer
from .models import DetailPermission
from permissions.serializers import PermisionSerializer
from scenarios.serializers import ScenarioSerializer


class DetailPermisosSerializer(ModelSerializer):
    escenario_id = ScenarioSerializer()
    permission_id = PermisionSerializer()

    class Meta:
        model = DetailPermission
        fields = "__all__"
