from rest_framework.serializers import ModelSerializer
from .models import  Permission


class PermisionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"





