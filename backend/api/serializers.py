from django.core.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from api.models import Communication, Crew, Schema, TodoList
from django.contrib.auth.models import User

import logging

logger = logging.getLogger("api")


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )


class RequestHelperMixin:
    @property
    def request(self):
        request = self.context.get("request")
        if not request:
            raise RuntimeError("request must be provided in the serializer context.")
        return request

    def get_user_crews(self):
        user = self.request.user
        if user.is_anonymous:
            raise RuntimeError("user must be authenticated.")

        return user.crews

    @property
    def user_crews(self):
        if not hasattr(self, "_crews"):
            self._crews = self.get_user_crews()

        return self._crews


class CrewContentSerializer(ModelSerializer, RequestHelperMixin):
    author = UserSerializer(read_only=True)
    crew = serializers.PrimaryKeyRelatedField(queryset=Crew.objects.all())

    def validate(self, data):
        crew = data.get("crew")
        if not self.user_crews.filter(pk=crew.pk).exists():
            raise ValidationError({"crew": "You do not belong to this crew."})

        return data

    def create(self, validated_data):
        validated_data["author"] = self.request.user
        return super().create(validated_data)


class CommunicationSerializer(CrewContentSerializer):
    class Meta:
        model = Communication
        fields = "__all__"


class SchemaSerializer(CrewContentSerializer):
    class Meta:
        model = Schema
        fields = "__all__"


class TodoListSerializer(CrewContentSerializer):
    class Meta:
        model = TodoList
        fields = "__all__"
