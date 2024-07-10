from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class UsuarioView(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

