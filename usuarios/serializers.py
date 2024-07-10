from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer
from .models import Usuario


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

    def create(self, validated_data):
        if "password" in validated_data:
            validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "password" in validated_data:
            validated_data["password"] = make_password(validated_data["password"])
        return super().update(instance, validated_data)


class LoginSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["email", "password"]
