"""Initialize models for Nautobot and ACI."""

from .nautobot import (
    NautobotApplicationProfile,
    NautobotApplicationTermination,
    NautobotBridgeDomain,
    NautobotDevice,
    NautobotDeviceRole,
    NautobotDeviceType,
    NautobotEPG,
    NautobotInterface,
    NautobotInterfaceTemplate,
    NautobotIPAddress,
    NautobotPrefix,
    NautobotTenant,
    NautobotVrf,
)

__all__ = [
    "NautobotTenant",
    "NautobotVrf",
    "NautobotDevice",
    "NautobotDeviceRole",
    "NautobotDeviceType",
    "NautobotInterfaceTemplate",
    "NautobotInterface",
    "NautobotPrefix",
    "NautobotIPAddress",
    "NautobotApplicationProfile",
    "NautobotBridgeDomain",
    "NautobotEPG",
    "NautobotApplicationTermination",
]
