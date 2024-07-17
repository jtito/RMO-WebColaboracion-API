from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer
from .models import Usuario
from rest_framework import serializers
from django.contrib.auth.hashers import check_password


class UserSerializer(ModelSerializer):
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


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password:
            try:
                user = Usuario.objects.get(email=email)
            except Usuario.DoesNotExist:
                raise serializers.ValidationError("Usuario no encontrado.")

            if not check_password(password, user.password):
                raise serializers.ValidationError("Datos invalidos")

            if not user.is_active:
                raise serializers.ValidationError("El usuario no está activo.")

        else:
            raise serializers.ValidationError(
                "Debe incluir tanto 'email' como 'password'."
            )

        data["user"] = user
        return data
