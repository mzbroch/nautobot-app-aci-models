"""App declaration for aci_models."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class AciModelsConfig(NautobotAppConfig):
    """App configuration for the aci_models app."""

    name = "aci_models"
    verbose_name = "Cisco ACI Models"
    version = __version__
    author = "Network to Code, LLC"
    description = "Cisco ACI Models."
    base_url = "aci-models"
    required_settings = []
    min_version = "2.0.0"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}


config = AciModelsConfig  # pylint:disable=invalid-name