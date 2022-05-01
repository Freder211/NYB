from rest_framework.serializers import ModelSerializer
from api.models import Communication
from django.contrib.auth.models import User


class CommunicationSerializer(ModelSerializer):

    class Meta:
        model = Communication
        fields = '__all__'
