"""Filtering for aci_models."""

from nautobot.apps.filters import NameSearchFilterSet, NautobotFilterSet

from aci_models import models


class ApplicationProfileFilterSet(NautobotFilterSet, NameSearchFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for ApplicationProfile."""

    class Meta:
        """Meta attributes for filter."""

        model = models.ApplicationProfile

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "description"]


class BridgeDomainFilterSet(NautobotFilterSet, NameSearchFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for BridgeDomain."""

    class Meta:
        """Meta attributes for filter."""

        model = models.BridgeDomain

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "description"]


class EPGFilterSet(NautobotFilterSet, NameSearchFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for EPG."""

    class Meta:
        """Meta attributes for filter."""

        model = models.EPG

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "description"]


class ApplicationTerminationFilterSet(NautobotFilterSet, NameSearchFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for ApplicationTermination."""

    class Meta:
        """Meta attributes for filter."""

        model = models.ApplicationTermination

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "description"]
