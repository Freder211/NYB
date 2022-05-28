from django.core.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from api.models import Communication, Crew, Schema, TodoItem, TodoList
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

        return user.crews.all()

    @property
    def user_crews(self):
        if not hasattr(self, "_crews"):
            self._crews = self.get_user_crews()

        return self._crews


class CrewHelperMixin(RequestHelperMixin):
    def is_user_member(self, crew):
        return self.user_crews.filter(pk=crew.pk).exists()


class CrewContentSerializer(ModelSerializer, CrewHelperMixin):
    author = UserSerializer(read_only=True)
    crew = serializers.PrimaryKeyRelatedField(queryset=Crew.objects.all())

    def validate(self, data):
        crew = data.get("crew")
        if not self.is_user_member(crew):
            raise ValidationError({"crew": "You do not belong to this crew."})

        return data

    def create(self, validated_data):
        validated_data["author"] = self.request.user
        return super().create(validated_data)


class CrewChildContentSerializer(ModelSerializer, CrewHelperMixin):
    @property
    def parent_field(self):
        return self.Meta.model.get_parent_field()

    def get_parent(self, validated_data):
        logger.debug(self.parent_field)
        return validated_data.get(self.parent_field)

    def validate(self, validated_data):
        parent = self.get_parent(validated_data)
        if not hasattr(parent, "crew"):
            raise ValueError("parent does not contain 'crew' field.")

        if not self.is_user_member(parent.crew):
            raise ValidationError(
                {self.parent_field: "You do not belong to this item's crew."}
            )
        return validated_data


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


class TodoItemSerializer(CrewChildContentSerializer):
    class Meta:
        model = TodoItem
        fields = "__all__"
        parent_field = "tdlist"
