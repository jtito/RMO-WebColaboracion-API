from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from .models import Usuario, PasswordResetToken
from .serializers import (
    UserGetSerializer,
    UserPostPutSerializer,
    LoginSerializer,
    PasswordResetRequestSerializer,
    PasswordResetSerializer
)
from .utils import get_tokens_for_user
from .email import send_email

# Asegúrate de tener las siguientes vistas:

class UserView(ModelViewSet):
    queryset = Usuario.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return UserPostPutSerializer
        return UserGetSerializer

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            user_serializer = UserGetSerializer(user)
            tokens = get_tokens_for_user(user)
            return Response({
                "user": user_serializer.data,
                "access_token": tokens["access"],
                "refresh_token": tokens["refresh"],
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

class CountryChoicesView(APIView):
    def get(self, request, *args, **kwargs):
        country_choices = Usuario.get_country_choices()
        formatted_choices = [
            {"value": value, "display_name": display_name}
            for value, display_name in country_choices
        ]
        return Response(formatted_choices)

class TypeDocChoicesView(APIView):
    def get(self, request, *args, **kwargs):
        type_doc_choices = Usuario.get_type_doc_choices()
        formatted_choices = [
            {"value": value, "display_name": display_name}
            for value, display_name in type_doc_choices
        ]
        return Response(formatted_choices)

class PasswordResetRequestView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        try:
            user = Usuario.objects.get(email=email)
            token = PasswordResetToken.objects.create(user=user)
            subject = "Restablecimiento de Contraseña"
            message = f"Tu código de restablecimiento de contraseña es: {token.token}"
            send_email(subject, message, user.email)
            return Response({"message": "Se ha enviado un código de restablecimiento a tu correo electrónico."}, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({"error": "El correo electrónico no está registrado."}, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            token = serializer.validated_data['token']
            new_password = serializer.validated_data['new_password']

            try:
                user = Usuario.objects.get(email=email)
                reset_token = PasswordResetToken.objects.get(user=user, token=token)
                if reset_token.is_expired():
                    return Response({"error": "El token ha expirado."}, status=status.HTTP_400_BAD_REQUEST)

                user.password = make_password(new_password)
                user.save()
                reset_token.delete()
                return Response({"message": "La contraseña ha sido restablecida exitosamente."}, status=status.HTTP_200_OK)
            except (Usuario.DoesNotExist, PasswordResetToken.DoesNotExist):
                return Response({"error": "Token inválido o usuario no encontrado."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)