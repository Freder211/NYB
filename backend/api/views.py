from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.models import Communication
from api.serializers import CommunicationSerializer


class CommunicationViewSet(ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer

