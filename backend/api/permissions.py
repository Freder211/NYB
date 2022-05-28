from django.contrib.auth.models import User
from django.views.generic.base import View
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet
from api.models import CrewContentModel

from logging import getLogger

logger = getLogger("api")


class CrewPermission(BasePermission):
    def has_permission(self, request: Request, view: View):
        user = request.user
        crew_pk = request.query_params.get("crew")
        if crew_pk:
            return user.crews.filter(pk=crew_pk).exists()
        return user.is_authenticated

    def has_object_permission(
        self, request: Request, view: View, obj: CrewContentModel
    ):

        if not isinstance(obj, CrewContentModel):
            raise ValueError("obj must be ModelOwnership subclass")

        user: User = request.user
        logger.debug(obj)

        try:
            crew_pk = obj.crew.pk
        except AttributeError:
            return False

        return user.crews.filter(pk=crew_pk).exists()


class CrewChildPermission(BaseException):
    # TODO: implemente permission
    pass
