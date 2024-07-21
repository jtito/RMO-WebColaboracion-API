from rest_framework.serializers import ModelSerializer
from .models import Role
from rest_framework import serializers
from permissions.models import DetailPermissionDocs
from permissions.serializers import DetailPermisosSerializer

class RolePostSerializer(ModelSerializer):
    detail_permisos = serializers.PrimaryKeyRelatedField(
        queryset=DetailPermissionDocs.objects.all(), many=True, write_only=True
    )

    class Meta:
        model = Role
        fields = "__all__"

    def create(self, validated_data):
        detail_permisos_ids = validated_data.pop("detail_permisos", [])
        role = super().create(validated_data)
        if detail_permisos_ids:
            role.detail_permisos.set(detail_permisos_ids)
        return role

    def update(self, instance, validated_data):
        detail_permisos_ids = validated_data.pop("detail_permisos", [])
        instance = super().update(instance, validated_data)
        if detail_permisos_ids:
            instance.detail_permisos.set(detail_permisos_ids)
        return instance


class RoleGetSerializer(ModelSerializer):
    detail_permisos = DetailPermisosSerializer(many=True, read_only=True)
    description = serializers.SerializerMethodField()

    class Meta:
        model = Role
        fields = "__all__"

    def get_description(self, obj):
        return dict(Role.ROLE_CHOICES).get(obj.description, "Unknown Role")

class RoleSerializer(serializers.Serializer):
    value = serializers.CharField()
    display_name = serializers.CharField()