"""Forms for aci_models."""
from django import forms
from nautobot.apps.forms import (
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
    NautobotBulkEditForm,
    NautobotFilterForm,
    NautobotModelForm,
    TagsBulkEditFormMixin,
)
from nautobot.dcim.models import Device, Interface
from nautobot.ipam.models import VLAN, VRF, IPAddress
from nautobot.tenancy.models import Tenant

from aci_models import models


class ApplicationProfileForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """ApplicationProfile creation/edit form."""

    tenant = DynamicModelChoiceField(queryset=Tenant.objects.all(), required=True)

    class Meta:
        """Meta attributes."""

        model = models.ApplicationProfile
        fields = [
            "name",
            "tenant",
            "description",
        ]


class ApplicationProfileBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """ACIModel bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.ApplicationProfile.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class ApplicationProfileFilterForm(NautobotFilterForm):
    """Filter form to filter searches."""

    model = models.ApplicationProfile
    tenant = DynamicModelMultipleChoiceField(
        queryset=Tenant.objects.all(),
        to_field_name="name",
        required=False,
        null_option="None",
    )

    field_order = ["q", "name", "tenant"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )
    name = forms.CharField(required=False, label="Name")


class BridgeDomainForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """BridgeDomain creation/edit form."""

    tenant = DynamicModelChoiceField(queryset=Tenant.objects.all(), required=True)
    vrf = DynamicModelChoiceField(
        queryset=VRF.objects.all(),
        label="VRF",
        required=True,
    )
    ip_addresses = DynamicModelMultipleChoiceField(
        queryset=IPAddress.objects.all(),
        required=False,
        label="IP Addresses",
    )

    class Meta:
        """Meta attributes."""

        model = models.BridgeDomain
        fields = [
            "name",
            "tenant",
            "vrf",
            "ip_addresses",
            "description",
        ]


class BridgeDomainBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """BridgeDomain bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.BridgeDomain.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class BridgeDomainFilterForm(NautobotFilterForm):
    """Filter form to filter searches."""
    tenant = DynamicModelMultipleChoiceField(
        queryset=Tenant.objects.all(),
        to_field_name="name",
        required=False,
        null_option="None",
    )

    vrf = DynamicModelMultipleChoiceField(
        queryset=VRF.objects.all(),
        to_field_name="name",
        required=False,
        null_option="None",
    )

    model = models.BridgeDomain
    field_order = ["q", "name", "tenant", "vrf"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )
    name = forms.CharField(required=False, label="Name")


class EPGForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """EPG creation/edit form."""

    tenant = DynamicModelChoiceField(queryset=Tenant.objects.all(), required=True)
    application = DynamicModelChoiceField(queryset=models.ApplicationProfile.objects.all(), required=True)
    bridge_domain = DynamicModelChoiceField(queryset=models.BridgeDomain.objects.all(), required=True)

    class Meta:
        """Meta attributes."""

        model = models.EPG
        fields = [
            "name",
            "tenant",
            "application",
            "bridge_domain",
            "description",
        ]


class EPGBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """ApplicationTermination bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.EPG.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class EPGFilterForm(NautobotFilterForm):
    """Filter form to filter searches."""

    model = models.EPG
    field_order = ["q", "name"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )
    name = forms.CharField(required=False, label="Name")


class ApplicationTerminationForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """ACIModel creation/edit form."""

    epg = DynamicModelChoiceField(queryset=models.EPG.objects.all(), required=True)
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
    )
    interface = DynamicModelChoiceField(
        queryset=Interface.objects.all(),
        query_params={"device_id": "$device"},
        help_text="Choose an interface to add to the Application Termination.",
    )
    vlan = DynamicModelChoiceField(
        queryset=VLAN.objects.all(),
        required=False,
        label="VLAN",
        # query_params={
        #     "locations": "$locations",
        #     "vlan_group": "$vlan_group",
        # },
    )
    class Meta:
        """Meta attributes."""

        model = models.ApplicationTermination
        fields = [
            "name",
            "epg",
            "device",
            "interface",
            "vlan",
            "description",
        ]

    def clean(self):
        pass
        # uniquness: interface and volan
        # how to check if vlan is onsite / same DC etc.


class ApplicationTerminationBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """ACIModel bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.ApplicationTermination.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class ApplicationTerminationFilterForm(NautobotFilterForm):
    """Filter form to filter searches."""

    model = models.ApplicationTermination
    field_order = ["q", "name"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )
    name = forms.CharField(required=False, label="Name")
    epg = DynamicModelMultipleChoiceField(
        queryset=models.EPG.objects.all(),
        to_field_name="name",
        required=False,
        null_option="None",
    )

    device = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        to_field_name="name",
        required=False,
        null_option="None",
    )
