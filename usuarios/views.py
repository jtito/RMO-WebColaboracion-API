from .models import Usuario
from .serializers import UsuarioSerializer, LoginSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class UsuarioView(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            return Response({"message": "Login exitoso"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
