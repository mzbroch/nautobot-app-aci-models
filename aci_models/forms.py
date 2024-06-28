"""Forms for aci_models."""
from django import forms
from nautobot.apps.forms import NautobotBulkEditForm, NautobotFilterForm, NautobotModelForm, TagsBulkEditFormMixin

from aci_models import models


class ACIModelForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """ACIModel creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = models.ACIModel
        fields = [
            "name",
            "description",
        ]


class ACIModelBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """ACIModel bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.ACIModel.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class ACIModelFilterForm(NautobotFilterForm):
    """Filter form to filter searches."""

    model = models.ACIModel
    field_order = ["q", "name"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )
    name = forms.CharField(required=False, label="Name")
