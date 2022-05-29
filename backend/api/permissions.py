from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from django.views.generic.base import View
from rest_framework import status
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet
from api.models import CrewContentModel, Crew

from logging import getLogger

logger = getLogger("api")


class CrewPermission(IsAuthenticated):
    def has_permission(self, request: Request, view: View):
        if not super().has_permission(request, view):
            return False

        user = request.user

        crew_pk = request.query_params.get("crew")
        if crew_pk:
            if not Crew.objects.filter(pk=crew_pk).exists():
                raise ValidationError(
                    {"detail": "The crew you requested does not exist."},
                    code=status.HTTP_404_NOT_FOUND,
                )

                return user.crews.filter(pk=crew_pk).exists()

        return True

    def has_object_permission(
        self, request: Request, view: View, obj: CrewContentModel
    ):

        if not isinstance(obj, CrewContentModel):
            raise ValueError("obj must be ModelOwnership subclass")

        user: User = request.user

        try:
            crew_pk = obj.crew.pk
        except AttributeError:
            return False

        return user.crews.filter(pk=crew_pk).exists()


class CrewChildPermission(CrewPermission):
    def has_object_permission(self, request, view, obj):
        parent = obj.parent
        return super().has_object_permission(request, view, parent)
