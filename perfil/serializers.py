from rest_framework.serializers import ModelSerializer
from .models import Perfil
from rest_framework import serializers
from permissions.serializers import DetailPermisosSerializer

class PerfilSerializer(ModelSerializer):
    detail_permisos = DetailPermisosSerializer(many=True, read_only = True)
    description = serializers.SerializerMethodField()
    class Meta:
        model = Perfil
        fields = "__all__"
    def get_description(self,obj):
        return obj.description


class PerfilSimpleSerializer(ModelSerializer):
    class Meta:
        model = Perfil
        fields = ['id','description']