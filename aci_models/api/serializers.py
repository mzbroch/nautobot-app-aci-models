"""API serializers for aci_models."""
from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin

from aci_models import models


class ACIModelSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """ACIModel Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.ACIModel
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
