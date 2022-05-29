from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.models import Communication, Schema, TodoItem, TodoList
from api.serializers import (
    CommunicationSerializer,
    SchemaSerializer,
    TodoItemSerializer,
    TodoListSerializer,
    UserSerializer,
)
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from django.contrib.auth import login, logout
from rest_framework import status

from logging import getLogger

from api.permissions import CrewChildPermission, CrewPermission

logger = getLogger("api")


class CrewContentViewSet(ModelViewSet):
    filter_fields = ["crew"]
    permission_classes = [CrewPermission]

    def current_action(self):
        method = self.request.method.lower()
        return self.action_map[method]

    def get_queryset(self):
        user = self.request.user

        if not isinstance(user, User):
            raise TypeError("A user must be provided to use this view")

        if self.current_action() == "list":
            return self.get_crew_fitlered_qs(user)

        return super().get_queryset()

    def get_crew_fitlered_qs(self, user):
        user_crews = user.crews.all()
        return (
            super(CrewContentViewSet, self).get_queryset().filter(crew__in=user_crews)
        )


class CrewChildContentViewSet(CrewContentViewSet):
    permission_classes = [CrewChildPermission]
    filter_fields = ["tdlist"]

    def get_crew_fitlered_qs(self, user):
        user_crews = user.crews.all()
        return self.queryset.filter(tdlist__crew__in=user_crews)


class CommunicationViewSet(CrewContentViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer


class SchemaViewSet(CrewContentViewSet):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer


class TodoListViewSet(CrewContentViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoItemViewSet(CrewChildContentViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


@api_view(["POST"])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def login_view(request):
    user = request.user
    login(request, user)
    user_data = UserSerializer(user).data
    return Response(user_data)


@api_view(["DELETE"])
@permission_classes([AllowAny])
def logout_view(request):
    logout(request)
    return Response(status=status.HTTP_204_NO_CONTENT)
