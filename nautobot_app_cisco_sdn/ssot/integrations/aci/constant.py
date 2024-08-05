"""Constants for use with the ACI SSoT app."""

from django.conf import settings

try:
    from nautobot_app_cisco_sdn.models import (
        ApplicationProfile,
        BridgeDomain,
        EPG,
        ApplicationTermination,
    )

    HAS_NAUTOBOT_APP_CISCO_SDN = True
except ImportError:
    HAS_NAUTOBOT_APP_CISCO_SDN = False


def _read_settings() -> dict:
    config = settings.PLUGINS_CONFIG["nautobot_app_cisco_sdn"]
    return {key[4:]: value for key, value in config.items() if key.startswith("aci_")}


# Import config vars from nautobot_config.py
PLUGIN_CFG = _read_settings()
