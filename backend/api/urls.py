from django.urls import path, include
from api.views import (
    CommunicationViewSet,
    ProConItemViewSet,
    ProConListViewSet,
    SchemaViewSet,
    TodoItemViewSet,
    TodoListViewSet,
    login_view,
    logout_view,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("communications", CommunicationViewSet)
router.register("schemas", SchemaViewSet)
router.register("todolists", TodoListViewSet)
router.register("todoitems", TodoItemViewSet)
router.register("proconlists", ProConListViewSet)
router.register("proconitems", ProConItemViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("login/", login_view),
    path("logout/", logout_view),
]
