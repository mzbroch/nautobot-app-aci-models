# pylint: disable=too-many-ancestors
"""Models for Cisco ACI Models."""

from django.db import models
from nautobot.apps.models import PrimaryModel

from .constants import CHARFIELD_MAX_LENGTH


class ApplicationProfile(PrimaryModel):
    """Represents Cisco ACI Application Profile."""

    name = models.CharField(max_length=CHARFIELD_MAX_LENGTH)
    tenant = models.ForeignKey(
        to="tenancy.Tenant",
        on_delete=models.PROTECT,
        related_name="aci_appprofiles",
    )
    description = models.CharField(max_length=CHARFIELD_MAX_LENGTH, blank=True)

    class Meta:
        """Meta class for ApplicationProfile."""

        verbose_name = "Cisco ACI Application Profile"
        verbose_name_plural = "Cisco ACI Application Profiles"
        ordering = ("name",)
        unique_together = ("tenant", "name")

    def __str__(self):
        """Return a string representation of the instance."""
        return self.name


class BridgeDomain(PrimaryModel):
    """Represents Cisco ACI Bridge Domain."""

    name = models.CharField(max_length=CHARFIELD_MAX_LENGTH)
    tenant = models.ForeignKey(
        to="tenancy.Tenant",
        on_delete=models.PROTECT,
        related_name="aci_bridgedomains",
    )
    vrf = models.ForeignKey(
        to="ipam.VRF",
        related_name="aci_bridgedomains",
        on_delete=models.PROTECT,
    )
    description = models.CharField(max_length=CHARFIELD_MAX_LENGTH, blank=True)
    ip_addresses = models.ManyToManyField(
        to="ipam.IPAddress",
        related_name="aci_bridgedomains",
        blank=True,
        verbose_name="IP Addresses",
    )

    class Meta:
        """Meta class for BridgeDomain."""

        verbose_name = "Cisco ACI Bridge Domain"
        verbose_name_plural = "Cisco ACI Bridge Domains"
        ordering = ("name",)
        unique_together = ("vrf", "name", "tenant")

    def __str__(self):
        """Return a string representation of the instance."""
        return self.name


class EPG(PrimaryModel):
    """Represents Cisco ACI EPG."""

    name = models.CharField(max_length=CHARFIELD_MAX_LENGTH)
    tenant = models.ForeignKey(
        to="tenancy.Tenant",
        on_delete=models.PROTECT,
        related_name="aci_epgs",
    )
    application = models.ForeignKey(
        ApplicationProfile,
        related_name="aci_epgs",
        on_delete=models.CASCADE,
    )
    bridge_domain = models.ForeignKey(
        BridgeDomain,
        related_name="aci_epgs",
        on_delete=models.CASCADE,
    )
    description = models.CharField(max_length=CHARFIELD_MAX_LENGTH, blank=True)

    class Meta:
        """Meta class for EPG."""

        verbose_name = "Cisco ACI EPG"
        verbose_name_plural = "Cisco ACI EPGs"
        ordering = ("name",)
        unique_together = ("name", "application", "tenant")

    def __str__(self):
        """Return a string representation of the instance."""
        return self.name


class ApplicationTermination(PrimaryModel):
    """Represents Cisco ACI Application Terminations."""

    epg = models.ForeignKey(
        EPG,
        related_name="aci_apptermination",
        on_delete=models.CASCADE,
    )
    interface = models.ForeignKey(
        to="dcim.Interface",
        related_name="aci_apptermination",
        on_delete=models.CASCADE,
    )

    @property
    def device(self):
        """Represents App-Terminating Device."""
        return self.interface.device if self.interface else None

    vlan = models.ForeignKey(
        to="ipam.VLAN",
        related_name="aci_apptermination",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=CHARFIELD_MAX_LENGTH,
        blank=True,
    )
    description = models.CharField(
        max_length=CHARFIELD_MAX_LENGTH,
        blank=True,
    )

    class Meta:
        """Meta class for ApplicationTermination."""

        verbose_name = "Cisco ACI App Termination"
        verbose_name_plural = "Cisco ACI App Termination"
        ordering = ("name",)
        unique_together = ("epg", "interface", "vlan")

    def __str__(self):
        """Return a string representation of the instance."""
        _vid = self.vlan.vid if self.vlan else 0

        return f"{self.interface.device.name}:{self.interface.name}:{_vid}"

    def clean(self):
        pass
        # vlan should be restricted to location (+child) of the device .
