"""API serializers for nautobot_app_cisco_sdn."""

from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin

from nautobot_app_cisco_sdn import models


class ApplicationProfileSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """ApplicationProfiler Model Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.ApplicationProfile
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []


class BridgeDomainSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """BridgeDomain Model Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.BridgeDomain
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []


class EPGSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """EPG Model Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.EPG
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []


class ApplicationTerminationSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """ApplicationTermination Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.ApplicationTermination
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
