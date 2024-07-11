from .models import Usuario
from .serializers import UsuarioSerializer, LoginSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from django.contrib.auth.hashers import check_password

# Create your views here.


class UsuarioView(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        user_request = LoginSerializer(data=request.data)
        if not user_request.is_valid():
            return Response({"message": user_request.errors}, status=401)
        
        user = Usuario.objects.get(email=user_request.data["email"])

        if not user:
            return Response({"message": "Email y/o password incorrectos"}, status=401)
        user_serializer = UsuarioSerializer(user).data
        
        if not check_password(
            user_request.data["password"], user_serializer.get("password")
        ):
            return Response({"message": "Email y/o password incorrectos"}, status=401)

        return Response(
            {
                "user": user_serializer,
            }
        )