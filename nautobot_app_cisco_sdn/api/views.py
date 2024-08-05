"""API views for nautobot_app_cisco_sdn."""

from nautobot.apps.api import NautobotModelViewSet

from nautobot_app_cisco_sdn import filters, models
from nautobot_app_cisco_sdn.api import serializers


class ApplicationProfileViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """ApplicationProfile viewset."""

    queryset = models.ApplicationProfile.objects.all()
    serializer_class = serializers.ApplicationProfileSerializer
    filterset_class = filters.ApplicationProfileFilterSet


class BridgeDomainViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """BridgeDomain viewset."""

    queryset = models.BridgeDomain.objects.all()
    serializer_class = serializers.BridgeDomainSerializer
    filterset_class = filters.BridgeDomainFilterSet


class EPGViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """EPG viewset."""

    queryset = models.EPG.objects.all()
    serializer_class = serializers.EPGSerializer
    filterset_class = filters.EPGFilterSet


class ApplicationTerminationViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """ApplicationTermination viewset."""

    queryset = models.ApplicationTermination.objects.all()
    serializer_class = serializers.ApplicationTerminationSerializer
    filterset_class = filters.ApplicationTerminationFilterSet
