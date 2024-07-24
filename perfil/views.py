from rest_framework.viewsets import ModelViewSet
from .models import Perfil
from .serializers import PerfilSerializer,PerfilSimpleSerializer
# Create your views here.


class PerfilView(ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    http_method_names=['get']
    

class PerfilSimpleView(ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSimpleSerializer
    http_method_names=['get']
