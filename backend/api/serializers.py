from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from api.models import Communication, Schema
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )


class OwnershipSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)


class CommunicationSerializer(OwnershipSerializer):
    class Meta:
        model = Communication
        fields = "__all__"


class SchemaSerializer(OwnershipSerializer):
    class Meta:
        model = Schema
        fields = "__all__"
