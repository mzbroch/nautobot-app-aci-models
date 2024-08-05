"""Utility functions for nautobot_app_cisco_sdn integrations."""

from importlib import import_module
from pathlib import Path
from types import ModuleType
from typing import Generator

from django.conf import settings

from nautobot_app_cisco_sdn.utils import logger


def each_enabled_integration() -> Generator[str, None, None]:
    """Return all enabled integrations."""
    config = settings.PLUGINS_CONFIG["nautobot_app_cisco_sdn"]

    for path in Path(__file__).parent.iterdir():
        if config.get(f"enable_{path.name}", False):
            yield path.name


def each_enabled_integration_module(module_name: str) -> Generator[ModuleType, None, None]:
    """For each enabled integration, import the module name."""
    for name in each_enabled_integration():
        try:
            module = import_module(f"nautobot_app_cisco_sdn.ssot.integrations.{name}.{module_name}")
        except ModuleNotFoundError:
            logger.debug("Integration %s does not have a %s module, skipping.", name, module_name)
            continue

        yield module