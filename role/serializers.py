from rest_framework.serializers import ModelSerializer
from .models import Role
from scenario_permissions.serializers import DetailPermisosSerializer
from rest_framework import serializers
class RoleSerializer(ModelSerializer):
    detail_permisos = DetailPermisosSerializer(many=True, read_only=True)
    description = serializers.SerializerMethodField()

    class Meta:
        model = Role
        fields = ['id', 'description', 'detail_permisos']

    def get_description(self,obj):
        return obj.description

   
class RoleSimpleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'description']