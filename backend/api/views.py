from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.models import Communication, Schema
from api.serializers import CommunicationSerializer, SchemaSerializer, UserSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import login, logout
from rest_framework import status


class OwnershipViewSet(ModelViewSet):

    def get_queryset(self):
        user = self.request.user

        if not isinstance(user, User):
            raise RuntimeError("A user must be provided to use this view")

        if self.request.method in SAFE_METHODS:
            return super().get_queryset()

        return super().get_queryset().filter(author=user)


class CommunicationViewSet(OwnershipViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer


class SchemaViewSet(OwnershipViewSet):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer


@api_view(["POST"])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def login_view(request):
    user = request.user
    login(request, user)
    user_data = UserSerializer(user).data
    return Response(user_data)


@api_view(["DELETE"])
def logout_view(request):
    logout(request)
    return Response(status=status.HTTP_204_NO_CONTENT)
