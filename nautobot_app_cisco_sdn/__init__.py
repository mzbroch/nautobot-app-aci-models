"""App declaration for nautobot_app_cisco_sdn."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

from nautobot_app_cisco_sdn.ssot.integrations.utils import each_enabled_integration_module
from nautobot_app_cisco_sdn.utils import logger

__version__ = metadata.version(__name__)


class NautobotAppCiscoSdnConfig(NautobotAppConfig):
    """App configuration for the nautobot_app_cisco_sdn app."""

    name = "nautobot_app_cisco_sdn"
    verbose_name = "Cisco ACI Models"
    version = __version__
    author = "Network to Code, LLC"
    description = "Cisco ACI Models."
    base_url = "nautobot-app-cisco-sdn"
    required_settings = []
    min_version = "2.0.0"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}

    def ready(self):
        """Trigger callback when database is ready."""
        super().ready()

        for module in each_enabled_integration_module("signals"):
            logger.debug("Registering signals for %s", module.__file__)
            module.register_signals(self)

config = NautobotAppCiscoSdnConfig  # pylint:disable=invalid-name
