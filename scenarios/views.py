from rest_framework.viewsets import ModelViewSet
from .models import Scenario
from .serializers import ScenarioSerializer
# Create your views here.
class ScenarioViewSet(ModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer
    http_method_names=['get']