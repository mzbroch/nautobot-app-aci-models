"""Forms for aci_models."""
from django import forms
from nautobot.apps.forms import NautobotBulkEditForm, NautobotFilterForm, NautobotModelForm, TagsBulkEditFormMixin, DynamicModelChoiceField, DynamicModelMultipleChoiceField
from nautobot.tenancy.models import Tenant
from nautobot.ipam.models import VRF
from nautobot.ipam.models import IPAddress

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
    field_order = ["q", "name"]

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

    model = models.BridgeDomain
    field_order = ["q", "name"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )
    name = forms.CharField(required=False, label="Name")


class EPGForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """EPG creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = models.EPG
        fields = [
            "name",
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

    class Meta:
        """Meta attributes."""

        model = models.ApplicationTermination
        fields = [
            "name",
            "description",
        ]


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
