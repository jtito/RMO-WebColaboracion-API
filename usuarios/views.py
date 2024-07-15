from .models import Usuario
from .serializers import UserSerializer, LoginSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuario
from .utils import get_tokens_for_user
from rest_framework import status

# Create your views here.


class UserView(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        print(f"Datos de solicitud recibidos: {request.data}")

        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            print("Serializer válido")

            user = serializer.validated_data['user']
            user_serializer = UserSerializer(user)
            tokens = get_tokens_for_user(user)
            return Response({
                "user": user_serializer.data,
                "access_token": tokens["access"],
                "refresh_token": tokens["refresh"],
            }, status=status.HTTP_200_OK)
        else:
            print(f"Errores de serializer: {serializer.errors}")

            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)