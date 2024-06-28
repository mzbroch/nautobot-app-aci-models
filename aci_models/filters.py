"""Filtering for aci_models."""

from nautobot.apps.filters import NameSearchFilterSet, NautobotFilterSet

from aci_models import models


class ACIModelFilterSet(NautobotFilterSet, NameSearchFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for ACIModel."""

    class Meta:
        """Meta attributes for filter."""

        model = models.ACIModel

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "description"]
