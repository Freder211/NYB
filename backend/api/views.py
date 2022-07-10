from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.models import Communication, ProConItem, ProConList, Schema, TodoItem, TodoList
from api.serializers import (
    CommunicationSerializer,
    ProConItemSerializer,
    ProConSerializer,
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

    def get_crew_fitlered_qs(self, user):
        user_crews = user.crews.all()
        filter_data = {f"{self.get_parent_field_name()}__crew__in": user_crews}
        return self.queryset.filter(**filter_data)

    def get_parent_field_name(self):
        parent_field_name = self.CrewMeta.parent_field_name
        if not parent_field_name:
            raise RuntimeError("parent_field_name must be defined")

        return parent_field_name

    class CrewMeta:
        parent_field_name = ""


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
    filter_fields = ["tdlist_id"]
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    class CrewMeta:
        parent_field_name = "tdlist_id"


class ProConListViewSet(CrewContentViewSet):
    queryset = ProConList.objects.all()
    serializer_class = ProConSerializer


class ProConItemViewSet(CrewChildContentViewSet):
    filter_fields = ["pclist_id"]
    queryset = ProConItem.objects.all()
    serializer_class = ProConItemSerializer

    class CrewMeta:
        parent_field_name = "pclist_id"


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
