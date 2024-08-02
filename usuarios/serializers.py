from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer
from .models import Usuario
from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from role.serializers import RoleSerializer
from role.models import Role

class UserGetSerializer(ModelSerializer):
    country_display = serializers.SerializerMethodField()
    type_doc_display = serializers.SerializerMethodField()

    role = RoleSerializer()

    class Meta:
        model = Usuario
        fields = ['id','role','name','last_nameF','last_nameS','country_display','type_doc_display','doc_num','email','is_active','create_at','updated_at']

    def get_type_doc_display(self, obj):
        return obj.get_type_doc_display()

    def get_country_display(self, obj):
        return obj.get_country_display()


class UserNameGetSerializer(ModelSerializer):
     class Meta:
        model = Usuario
        fields = ['name','last_nameF','last_nameS']

class UserPostPutSerializer(ModelSerializer):
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())

    class Meta:
        model = Usuario
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

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


class CountrySerializer(serializers.Serializer):
    value = serializers.CharField()
    display_name = serializers.CharField()


class TypeDocSerializer(serializers.Serializer):
    value = serializers.CharField()
    display_name = serializers.CharField()
