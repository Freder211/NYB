from django.contrib.auth.models import User
from django.views.generic.base import View
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from backend.api.models import CrewContentModel


class CrewPermission(BasePermission):
    def has_permission(self, request: Request, view: View):
        user: User = request.user
        return user.is_authenticated

    def has_object_permission(
        self, request: Request, view: View, obj: CrewContentModel
    ):

        if not isinstance(obj, CrewContentModel):
            raise ValueError("obj must be ModelOwnership subclass")

        user: User = request.user
        crew_pk = obj.crew.pk
        return user.crews.filter(pk=crew_pk).exist()
