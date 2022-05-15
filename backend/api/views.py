from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.models import Communication
from api.serializers import CommunicationSerializer


class CommunicationViewSet(ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        if not isinstance(user, User):
            raise RuntimeError("A user must be provided to use this view")
        return super().get_queryset().filter(author=user)
