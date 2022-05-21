from django.urls import path, include
from api.views import CommunicationViewSet, SchemaViewSet, login_view, logout_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("communications", CommunicationViewSet)
router.register("schemas", SchemaViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("login/", login_view),
    path("logout/", logout_view),
]
