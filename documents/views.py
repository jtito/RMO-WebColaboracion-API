from rest_framework.viewsets import ModelViewSet
from .models import Document, PerfilDocument, TypeDocument, StateDocument
from .serializers import (
    DocumentGETSerializer,
    DocumentPOSTSerializer,
    PerfilxDocsGETSerializer,
    PerfilxDocsPOSTSerializer,
    TypeDocumentGETSerializer,
    StateDocumentGETSerializer,
)

# Create your views here.


class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return DocumentPOSTSerializer
        return DocumentGETSerializer


class TypeDocumentViewSet(ModelViewSet):
    queryset = TypeDocument.objects.all()
    serializer_class = TypeDocumentGETSerializer
    http_method_names = ["get"]


# Create your views here.


class PerfilxDocsViewSet(ModelViewSet):
    queryset = PerfilDocument.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return PerfilxDocsPOSTSerializer
        return PerfilxDocsGETSerializer



class StateViewSet(ModelViewSet):
    queryset = StateDocument.objects.all()
    serializer_class = StateDocumentGETSerializer
    http_method_names = ["get"]
