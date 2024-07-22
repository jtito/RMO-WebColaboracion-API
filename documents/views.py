from rest_framework.viewsets import ModelViewSet
from .models import Document
from .serializers import DocumentSerializer

# Create your views here.


class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    http_method_names=['get']
# Create your views here.
