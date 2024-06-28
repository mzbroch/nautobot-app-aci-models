"""Tables for aci_models."""

import django_tables2 as tables
from nautobot.apps.tables import BaseTable, ButtonsColumn, ToggleColumn

from aci_models import models


class ApplicationProfileTable(BaseTable):
    # pylint: disable=R0903
    """Table for ApplicationProfile list view."""

    pk = ToggleColumn()
    name = tables.Column(linkify=True)
    actions = ButtonsColumn(
        models.ApplicationProfile,
        # Option for modifying the default action buttons on each row:
        # buttons=("changelog", "edit", "delete"),
        # Option for modifying the pk for the action buttons:
        pk_field="pk",
    )

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.ApplicationProfile
        fields = (
            "pk",
            "name",
            "description",
        )

        # Option for modifying the columns that show up in the list view by default:
        # default_columns = (
        #     "pk",
        #     "name",
        #     "description",
        # )

class BridgeDomainTable(BaseTable):
    # pylint: disable=R0903
    """Table for BridgeDomain list view."""

    pk = ToggleColumn()
    name = tables.Column(linkify=True)
    actions = ButtonsColumn(
        models.BridgeDomain,
        # Option for modifying the default action buttons on each row:
        # buttons=("changelog", "edit", "delete"),
        # Option for modifying the pk for the action buttons:
        pk_field="pk",
    )

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.BridgeDomain
        fields = (
            "pk",
            "name",
            "description",
        )

        # Option for modifying the columns that show up in the list view by default:
        # default_columns = (
        #     "pk",
        #     "name",
        #     "description",
        # )

class EPGTable(BaseTable):
    # pylint: disable=R0903
    """Table for EPG list view."""

    pk = ToggleColumn()
    name = tables.Column(linkify=True)
    actions = ButtonsColumn(
        models.EPG,
        # Option for modifying the default action buttons on each row:
        # buttons=("changelog", "edit", "delete"),
        # Option for modifying the pk for the action buttons:
        pk_field="pk",
    )

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.EPG
        fields = (
            "pk",
            "name",
            "description",
        )

        # Option for modifying the columns that show up in the list view by default:
        # default_columns = (
        #     "pk",
        #     "name",
        #     "description",
        # )

class ApplicationTerminationTable(BaseTable):
    # pylint: disable=R0903
    """Table for ApplicationTermination list view."""

    pk = ToggleColumn()
    name = tables.Column(linkify=True)
    actions = ButtonsColumn(
        models.ApplicationTermination,
        # Option for modifying the default action buttons on each row:
        # buttons=("changelog", "edit", "delete"),
        # Option for modifying the pk for the action buttons:
        pk_field="pk",
    )

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.ApplicationTermination
        fields = (
            "pk",
            "name",
            "description",
        )

        # Option for modifying the columns that show up in the list view by default:
        # default_columns = (
        #     "pk",
        #     "name",
        #     "description",
        # )
