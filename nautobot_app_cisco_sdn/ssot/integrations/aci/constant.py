"""Constants for use with the ACI SSoT app."""
from importlib.util import find_spec

from django.conf import settings

aci_models = "nautobot_app_cisco_sdn.models"

def module_exists(module: str) -> bool:
    """_summary_.

    Args:
        module (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        find_spec(module)
        return True
    except ModuleNotFoundError:
        return False

def _read_settings() -> dict:
    """_summary_.

    Returns:
        dict: _description_
    """
    config = settings.PLUGINS_CONFIG["nautobot_app_cisco_sdn"]
    return {key[4:]: value for key, value in config.items() if key.startswith("aci_")}

# Check if Nautobot ACI models exist
HAS_NAUTOBOT_APP_CISCO_SDN = module_exists(aci_models)
# Import config vars from nautobot_config.py
PLUGIN_CFG = _read_settings()
