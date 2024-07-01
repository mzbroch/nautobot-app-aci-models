"""Tables for aci_models."""

import django_tables2 as tables
from nautobot.apps.tables import BaseTable, ButtonsColumn, ToggleColumn

from nautobot.tenancy.tables import TenantColumn

from aci_models import models

APPTERM_LINK = """
<a href="{% url 'plugins:aci_models:applicationtermination' pk=record.pk %}">
    {{ record.name|default:'<span class="label label-info">Unnamed EPG</span>' }}
</a>
"""

class ApplicationProfileTable(BaseTable):
    # pylint: disable=R0903
    """Table for ApplicationProfile list view."""

    pk = ToggleColumn()
    name = tables.Column(linkify=True)
    tenant = TenantColumn()
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
            "tenant",
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
    tenant = TenantColumn()
    vrf = tables.Column(verbose_name="VRF", linkify=lambda record: record.vrf.get_absolute_url(), accessor="vrf.name")
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
            "tenant",
            "vrf",
            "ip_addresses",
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
    tenant = TenantColumn()
    application = tables.Column(linkify=True)
    bridge_domain = tables.Column(linkify=True)
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
            "tenant",
            "application",
            "bridge_domain",
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
    name = tables.TemplateColumn(template_code=APPTERM_LINK)
    epg = tables.Column(verbose_name="EPG", linkify=True)
    device = tables.Column(linkify=True)
    interface = tables.Column(linkify=True)
    vlan = tables.Column(verbose_name="VLAN", linkify=True)
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
            "epg",
            "device",
            "interface",
            "vlan",
            "description",
        )

        # Option for modifying the columns that show up in the list view by default:
        # default_columns = (
        #     "pk",
        #     "name",
        #     "description",
        # )
