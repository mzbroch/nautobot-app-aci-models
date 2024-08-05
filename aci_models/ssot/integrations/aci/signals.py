"""Signals for ACI integration."""

# pylint: disable=logging-fstring-interpolation, invalid-name
import logging
import random

from django.dispatch import receiver
from django.db.models.signals import post_save
from nautobot.core.signals import nautobot_database_ready
from nautobot.extras.choices import CustomFieldTypeChoices

from nautobot.dcim.models.devices import Controller
from nautobot.extras.models import Tag
from aci_models.ssot.integrations.aci.constant import PLUGIN_CFG

logger = logging.getLogger("nautobot.ssot.aci")


def register_signals(sender):
    """Registers signals."""
    nautobot_database_ready.connect(aci_create_tag, sender=sender)
    nautobot_database_ready.connect(aci_create_manufacturer, sender=sender)
    nautobot_database_ready.connect(aci_create_location_type, sender=sender)
    nautobot_database_ready.connect(device_custom_fields, sender=sender)
    nautobot_database_ready.connect(interface_custom_fields, sender=sender)

@receiver(post_save, sender=Controller)
def controller_created(sender, instance, created, **kwargs):
    if created and instance.external_integration:
        extra_config = instance.external_integration.extra_config
        if "tag" in extra_config.keys():
            logger.info("Creating tags for ACI, interface status and Sites")
            Tag.objects.update_or_create(
                name=extra_config.get("tag"),
                color=PLUGIN_CFG.get("tag_color"),
            )           

def aci_create_tag(apps, **kwargs):
    """Add a tag."""
    tag = apps.get_model("extras", "Tag")
    logger.info("Creating tags for ACI, interface status and Sites")

    tag.objects.update_or_create(
        name=PLUGIN_CFG.get("tag"),
        color=PLUGIN_CFG.get("tag_color"),
    )
    tag.objects.update_or_create(
        name=PLUGIN_CFG.get("tag_up"),
        color=PLUGIN_CFG.get("tag_up_color"),
    )
    tag.objects.update_or_create(
        name=PLUGIN_CFG.get("tag_down"),
        color=PLUGIN_CFG.get("tag_down_color"),
    )
    tag.objects.update_or_create(
        name="ACI_MULTISITE",
        color="03a9f4",
    )

def aci_create_manufacturer(apps, **kwargs):
    """Add manufacturer."""
    manufacturer = apps.get_model("dcim", "Manufacturer")
    logger.info(f"Creating manufacturer: {PLUGIN_CFG.get('manufacturer_name')}")
    manufacturer.objects.update_or_create(
        name=PLUGIN_CFG.get("manufacturer_name"),
    )

def aci_create_location_type(apps, **kwargs):
    """Add site."""
    ContentType = apps.get_model("contenttypes", "ContentType")
    Controller = apps.get_model("dcim", "Controller")
    Rack = apps.get_model("dcim", "Rack")
    Device = apps.get_model("dcim", "Device")
    Namespace = apps.get_model("ipam", "Namespace")
    Prefix = apps.get_model("ipam", "Prefix")
    Vlan = apps.get_model("ipam", "VLAN")
    LocationType = apps.get_model("dcim", "LocationType")
    
    loc_type = LocationType.objects.update_or_create(name="Datacenter")[0]

    for model in [Controller, Rack, Device, Namespace, Prefix, Vlan]:
        loc_type.content_types.add(ContentType.objects.get_for_model(model))

def device_custom_fields(apps, **kwargs):
    """Creating custom fields for interfaces."""
    ContentType = apps.get_model("contenttypes", "ContentType")
    Device = apps.get_model("dcim", "Device")
    CustomField = apps.get_model("extras", "CustomField")
    logger.info("Creating Device extra fields for PodID and NodeID")

    for device_cf_dict in [
        {
            "key": "aci_pod_id",
            "type": CustomFieldTypeChoices.TYPE_INTEGER,
            "label": "Cisco ACI Pod ID",
            "filter_logic": "loose",
            "description": "PodID added by SSoT app",
        },
        {
            "key": "aci_node_id",
            "type": CustomFieldTypeChoices.TYPE_INTEGER,
            "label": "Cisco ACI Node ID",
            "filter_logic": "loose",
            "description": "NodeID added by SSoT app",
        },
    ]:
        field, _ = CustomField.objects.get_or_create(key=device_cf_dict["key"], defaults=device_cf_dict)
        field.content_types.set([ContentType.objects.get_for_model(Device)])


def interface_custom_fields(apps, **kwargs):
    """Creating custom fields for interfaces."""
    ContentType = apps.get_model("contenttypes", "ContentType")
    Interface = apps.get_model("dcim", "Interface")
    CustomField = apps.get_model("extras", "CustomField")
    logger.info("Creating Interface extra fields for Optics")

    for interface_cf_dict in [
        {
            "key": "gbic_vendor",
            "type": CustomFieldTypeChoices.TYPE_TEXT,
            "label": "Optic Vendor",
            "filter_logic": "loose",
            "description": "Optic vendor added by SSoT app",
        },
        {
            "key": "gbic_type",
            "type": CustomFieldTypeChoices.TYPE_TEXT,
            "label": "Optic Type",
            "filter_logic": "loose",
            "description": "Optic type added by SSoT app",
        },
        {
            "key": "gbic_sn",
            "type": CustomFieldTypeChoices.TYPE_TEXT,
            "label": "Optic S/N",
            "filter_logic": "loose",
            "description": "Optic S/N added by SSoT app",
        },
        {
            "key": "gbic_model",
            "type": CustomFieldTypeChoices.TYPE_TEXT,
            "label": "Optic Model",
            "filter_logic": "loose",
            "description": "Optic Model added by SSoT app",
        },
    ]:
        field, _ = CustomField.objects.get_or_create(key=interface_cf_dict["key"], defaults=interface_cf_dict)
        field.content_types.set([ContentType.objects.get_for_model(Interface)])
