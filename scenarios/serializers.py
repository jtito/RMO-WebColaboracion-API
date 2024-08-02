from rest_framework.serializers import ModelSerializer
from .models import Scenario
class ScenarioSerializer(ModelSerializer):
    class Meta:
        model = Scenario
        fields = "__all__"
    