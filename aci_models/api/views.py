"""API views for aci_models."""

from nautobot.apps.api import NautobotModelViewSet

from aci_models import filters, models
from aci_models.api import serializers


class ACIModelViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """ACIModel viewset."""

    queryset = models.ACIModel.objects.all()
    serializer_class = serializers.ACIModelSerializer
    filterset_class = filters.ACIModelFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
