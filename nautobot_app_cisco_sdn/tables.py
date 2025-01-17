"""Tables for nautobot_app_cisco_sdn."""

import django_tables2 as tables
from nautobot.apps.tables import BaseTable, ButtonsColumn, ToggleColumn
from nautobot.tenancy.tables import TenantColumn

from nautobot_app_cisco_sdn import models

APPTERM_LINK = """
<a href="{% url 'plugins:nautobot_app_cisco_sdn:applicationtermination' pk=record.pk %}">
    {{ record.name|default:'<span class="label label-info">Unnamed App. Term.</span>' }}
</a>
"""
BD_IPADDRESS_LINK = """
{% for ipaddress in record.ip_addresses.all %}
    <a href="{% url 'ipam:ipaddress' pk=ipaddress.pk %}">{{ ipaddress }}</a>{% if not forloop.last %}<br />{% endif %}
{% empty %}
    &mdash;
{% endfor %}
"""


class ApplicationProfileTable(BaseTable):
    # pylint: disable=R0903
    """Table for ApplicationProfile list view."""

    pk = ToggleColumn()
    name = tables.Column(linkify=True)
    tenant = TenantColumn()
    actions = ButtonsColumn(
        models.ApplicationProfile,
        pk_field="pk",
    )

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.ApplicationProfile
        fields = (  # pylint: disable=nb-use-fields-all
            "pk",
            "name",
            "tenant",
            "description",
        )


class BridgeDomainTable(BaseTable):
    # pylint: disable=R0903
    """Table for BridgeDomain list view."""
    pk = ToggleColumn()
    name = tables.Column(linkify=True)
    tenant = TenantColumn()
    vrf = tables.Column(
        verbose_name="VRF",
        linkify=lambda record: record.vrf.get_absolute_url(),
        accessor="vrf.name",
    )
    ip_addresses = tables.TemplateColumn(
        template_code=BD_IPADDRESS_LINK,
        orderable=False,
        verbose_name="IP Addresses",
    )
    actions = ButtonsColumn(
        models.BridgeDomain,
        pk_field="pk",
    )

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.BridgeDomain
        fields = (  # pylint: disable=nb-use-fields-all
            "pk",
            "name",
            "tenant",
            "vrf",
            "ip_addresses",
            "description",
        )


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
        pk_field="pk",
    )

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.EPG
        fields = (  # pylint: disable=nb-use-fields-all
            "pk",
            "name",
            "tenant",
            "application",
            "bridge_domain",
            "description",
        )


class ApplicationTerminationTable(BaseTable):
    # pylint: disable=R0903
    """Table for ApplicationTermination list view."""

    pk = ToggleColumn()
    name = tables.TemplateColumn(template_code=APPTERM_LINK)
    epg = tables.Column(verbose_name="EPG", linkify=True)
    epg__application__name = tables.Column(verbose_name="Application Name", linkify=True)
    device = tables.Column(linkify=True)
    interface = tables.Column(linkify=True)
    vlan = tables.Column(verbose_name="VLAN", linkify=True)
    actions = ButtonsColumn(
        models.ApplicationTermination,
        pk_field="pk",
    )

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.ApplicationTermination
        fields = (  # pylint: disable=nb-use-fields-all
            "pk",
            "name",
            "epg",
            "epg__application__name",
            "device",
            "interface",
            "vlan",
            "description",
        )
