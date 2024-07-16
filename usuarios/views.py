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
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            user_serializer = UserSerializer(user)
            tokens = get_tokens_for_user(user)
            return Response({
                "user": user_serializer.data,
                "access_token": tokens["access"],
                "refresh_token": tokens["refresh"],
            }, status=status.HTTP_200_OK)
        else:

            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        

class CountryChoicesView(APIView):
    def get(self, request, *args, **kwargs):
        country_choices = Usuario.get_country_choices()
        formatted_choices = [
            {"value": value, "display_name": display_name}
            for value, display_name in country_choices
        ]
        return Response(formatted_choices)

class RoleChoicesView(APIView):
    def get(self, request, *args, **kwargs):
        role_choices = Usuario.get_role_choices()
        formatted_choices = [
            {"value": value, "display_name": display_name}
            for value, display_name in role_choices
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