"""Filtering for aci_models."""

from nautobot.apps.filters import NameSearchFilterSet, NautobotFilterSet
from nautobot.core.filters import NaturalKeyOrPKMultipleChoiceFilter
from nautobot.dcim.models import Device
from nautobot.ipam.models import VRF
from nautobot.tenancy.models import Tenant

from aci_models import models


class ApplicationProfileFilterSet(NautobotFilterSet, NameSearchFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for ApplicationProfile."""
    tenant = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        to_field_name="name",
        label="Tenant (name or ID)",
    )

    class Meta:
        """Meta attributes for filter."""

        model = models.ApplicationProfile

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "description"]


class BridgeDomainFilterSet(NautobotFilterSet, NameSearchFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for BridgeDomain."""
    tenant = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        to_field_name="name",
        label="Tenant (name or ID)",
    )
    vrf = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=VRF.objects.all(),
        to_field_name="name",
        label="VRF (ID or name)",
    )

    class Meta:
        """Meta attributes for filter."""

        model = models.BridgeDomain

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "description"]


class EPGFilterSet(NautobotFilterSet, NameSearchFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for EPG."""
    tenant = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        to_field_name="name",
        label="Tenant (name or ID)",
    )
    application = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=models.ApplicationProfile.objects.all(),
        to_field_name="name",
        label="ApplicationProfile (name or ID)",
    )
    bridge_domain = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=models.BridgeDomain.objects.all(),
        to_field_name="name",
        label="BridgeDomain (name or ID)",
    )

    class Meta:
        """Meta attributes for filter."""

        model = models.EPG

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "description"]


class ApplicationTerminationFilterSet(NautobotFilterSet, NameSearchFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for ApplicationTermination."""

    epg = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=models.EPG.objects.all(),
        to_field_name="name",
        label="EPG (name or ID)",
    )
    device = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=Device.objects.all(),
        to_field_name="name",
        field_name="interface__device",
        label="Device (name or ID)",
    )

    class Meta:
        """Meta attributes for filter."""

        model = models.ApplicationTermination

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "description"]
