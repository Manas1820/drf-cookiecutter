from drf_psq import PsqMixin, Rule
from rest_framework import status
from rest_framework.mixins import UpdateModelMixin, CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from {{ cookiecutter.project_slug }}.apps.{{ cookiecutter.app_name }}.models.user_models import Item
from {{ cookiecutter.project_slug }}.apps.{{ cookiecutter.app_name }}.serializers import (
    ItemsSerializer,
)


class ItemsViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, PsqMixin, GenericViewSet):
    http_method_names = ["patch"]
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    psq_rules = {
        "list": [Rule([AllowAny], ItemsSerializer)],
        "retrieve": [Rule([AllowAny], ItemsSeriazlier)],
        "create": [Rule([AllowAny], ItemsSeriazlier)],
        "partial_update": [Rule([AllowAny], ItemsSeriazlier)],
        "publish": [Rule([AllowAny], ItemsSeriazlier)],
    }

    def get_queryset(self):
        return Item.objects.all()
