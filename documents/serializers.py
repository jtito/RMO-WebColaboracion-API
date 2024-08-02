from rest_framework.serializers import ModelSerializer
from .models import Document, PerfilDocument, TypeDocument, StateDocument
from rest_framework import serializers
from usuarios.models import Usuario
from usuarios.serializers import UserNameGetSerializer
from perfil.models import Perfil
from perfil.serializers import PerfilSerializer

class StateDocumentGETSerializer(ModelSerializer):
    class Meta:
        model = StateDocument
        fields = "__all__"


class TypeDocumentGETSerializer(ModelSerializer):
    class Meta:
        model = TypeDocument
        fields = "__all__"


class PerfilxDocsGETSerializer(ModelSerializer):
    
    user = UserNameGetSerializer()
    perfil = PerfilSerializer()

    class Meta:
        model = PerfilDocument
        fields = ['id','user', 'perfil']


class PerfilxDocsPOSTSerializer(ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    perfil = serializers.PrimaryKeyRelatedField(queryset=Perfil.objects.all())

    class Meta:
        model = PerfilDocument
        fields = "__all__"


class DocumentGETSerializer(ModelSerializer):
    typeDoc = TypeDocumentGETSerializer()
    user_perfil = PerfilxDocsGETSerializer(many=True) 
    state = StateDocumentGETSerializer()

    class Meta:
        model = Document
        fields = "__all__"


class DocumentPOSTSerializer(ModelSerializer):
    typeDoc = serializers.PrimaryKeyRelatedField(queryset=TypeDocument.objects.all())
    state = serializers.PrimaryKeyRelatedField(queryset=StateDocument.objects.all())
    user_perfil = serializers.PrimaryKeyRelatedField(
        queryset=PerfilDocument.objects.all(), many=True, required=False, allow_null = True
    )

    class Meta:
        model = Document
        fields = "__all__"

    def create(self, validated_data):
        user_perfil_data = validated_data.pop("user_perfil", [])
        document = Document.objects.create(**validated_data)
        document.user_perfil.set(user_perfil_data)  # Set the many-to-many relationships
        return document

    def update(self, instance, validated_data):
        user_perfil_data = validated_data.pop("user_perfil", [])
        instance = super().update(instance, validated_data)
        instance.user_perfil.set(
            user_perfil_data
        )  # Update the many-to-many relationships
        return instance
