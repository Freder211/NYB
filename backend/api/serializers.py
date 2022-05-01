from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from api.models import Communication
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class CommunicationSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Communication
        fields = '__all__'
