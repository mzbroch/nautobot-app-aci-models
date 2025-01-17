"""DiffSync Adapter for Nautobot."""

# pylint: disable=duplicate-code

import logging
from collections import defaultdict

from diffsync import Adapter
from diffsync.enum import DiffSyncModelFlags
from django.contrib.contenttypes.models import ContentType
from django.db.models import ProtectedError
from nautobot.dcim.models import Device, DeviceType, Interface, InterfaceTemplate
from nautobot.extras.models import Role
from nautobot.ipam.models import VRF, IPAddress, Prefix
from nautobot.tenancy.models import Tenant

from nautobot_app_cisco_sdn.ssot.integrations.aci.constant import HAS_NAUTOBOT_APP_CISCO_SDN, PLUGIN_CFG
from nautobot_app_cisco_sdn.ssot.integrations.aci.diffsync.models import (
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

if HAS_NAUTOBOT_APP_CISCO_SDN:
    from nautobot_app_cisco_sdn.models import (
        EPG,
        ApplicationProfile,
        ApplicationTermination,
        BridgeDomain,
    )

logger = logging.getLogger(__name__)


class NautobotAdapter(Adapter):
    """Nautobot adapter for DiffSync."""

    objects_to_delete = defaultdict(list)

    tenant = NautobotTenant
    vrf = NautobotVrf
    device_type = NautobotDeviceType
    device_role = NautobotDeviceRole
    device = NautobotDevice
    interface_template = NautobotInterfaceTemplate
    interface = NautobotInterface
    ip_address = NautobotIPAddress
    prefix = NautobotPrefix
    aci_appprofile = NautobotApplicationProfile
    aci_bridgedomain = NautobotBridgeDomain
    aci_epg = NautobotEPG
    aci_apptermination = NautobotApplicationTermination

    top_level = [
        "tenant",
        "vrf",
        "device_type",
        "device_role",
        "interface_template",
        "device",
        "interface",
        "prefix",
        "ip_address",
        "aci_appprofile",
        "aci_bridgedomain",
        "aci_epg",
        "aci_apptermination",
    ]

    def __init__(self, *args, job=None, sync=None, site_name: str, site_type: str, controller_tag: str, **kwargs):  # noqa: PLR0913 # pylint: disable=R0913
        """Initialize Nautobot.

        Args:
            job (object, optional): Nautobot job. Defaults to None.
            sync (object, optional): Nautobot DiffSync. Defaults to None.
            site_name (str): Name of Site to filter objects on.
            site_type (str): location type.
            controller_tag (str): tag for controller created objects.
            *args: None.
            **kwargs: None.
        """
        super().__init__(*args, **kwargs)
        self.job = job
        self.sync = sync
        self.site = site_name
        self.site_type = site_type
        self.controller_tag = controller_tag

    def sync_complete(self, source: Adapter, *args, **kwargs):
        """Clean up function for DiffSync sync.

        Once the sync is complete, this function runs deleting any objects
        from Nautobot that need to be deleted in a specific order.

        Args:
            source (Adapter): DiffSync Adapter
            *args: None.
            **kwargs: None.
        """
        for grouping in (
            "aci_apptermination",
            "aci_epg",
            "aci_bridgedomain",
            "aci_appprofile",
            "ipaddress",
            "prefix",
            "vrf",
            "tenant",
            "device",
        ):
            for nautobot_object in self.objects_to_delete[grouping]:
                try:
                    logger.warning("OBJECT: %s", nautobot_object)
                    nautobot_object.delete()
                except ProtectedError:
                    self.job.logger.error("Deletion failed protected object")
            self.objects_to_delete[grouping] = []

        return super().sync_complete(source, *args, **kwargs)

    def load_tenants(self):
        """Method to load Tenants from Nautobot."""
        for nbtenant in Tenant.objects.filter(tags__name=self.controller_tag):
            _tenant = self.tenant(
                name=nbtenant.name,
                description=nbtenant.description,
                comments=nbtenant.comments,
                controller_tag=self.controller_tag,
                msite_tag=nbtenant.tags.filter(name="ACI_MULTISITE").exists(),
            )
            self.add(_tenant)

    def load_vrfs(self):
        """Method to load VRFs from Nautobot."""
        for nbvrf in VRF.objects.filter(tags__name=self.controller_tag):
            _vrf = self.vrf(
                name=nbvrf.name,
                namespace=nbvrf.namespace.name,
                tenant=nbvrf.tenant.name,
                description=nbvrf.description if not None else "",
                controller_tag=self.controller_tag,
            )
            self.add(_vrf)

    def load_devicetypes(self):
        """Method to load Device Types from Nautobot."""
        sor_tag = PLUGIN_CFG.get("tag", "SoR:CiscoACI")
        for nbdevicetype in DeviceType.objects.filter(tags__name=sor_tag):
            _devicetype = self.device_type(
                model=nbdevicetype.model,
                part_nbr=nbdevicetype.part_number,
                manufacturer=nbdevicetype.manufacturer.name,
                comments=nbdevicetype.comments,
                u_height=nbdevicetype.u_height,
            )
            self.add(_devicetype)

    def load_interfacetemplates(self):
        """Method to load Interface Templates from Nautobot."""
        for nbinterfacetemplate in InterfaceTemplate.objects.filter(tags__name=self.controller_tag):
            _interfacetemplate = self.interface_template(
                name=nbinterfacetemplate.name,
                device_type=nbinterfacetemplate.device_type.model,
                type=nbinterfacetemplate.type,
                mgmt_only=nbinterfacetemplate.mgmt_only,
                controller_tag=self.controller_tag,
            )
            self.add(_interfacetemplate)

    def load_interfaces(self):
        """Method to load Interfaces from Nautobot."""
        for nbinterface in Interface.objects.filter(tags__name=self.controller_tag):
            if nbinterface.tags.filter(name=PLUGIN_CFG.get("tag_up")).count() > 0:
                state = PLUGIN_CFG.get("tag_up").lower().replace(" ", "-")
            else:
                state = PLUGIN_CFG.get("tag_down").lower().replace(" ", "-")
            _interface = self.interface(
                name=nbinterface.name,
                device=nbinterface.device.name,
                site=nbinterface.device.location.name,
                description=nbinterface.description,
                gbic_vendor=nbinterface.custom_field_data.get("gbic_vendor", ""),
                gbic_type=nbinterface.custom_field_data.get("gbic_type", ""),
                gbic_sn=nbinterface.custom_field_data.get("gbic_sn", ""),
                gbic_model=nbinterface.custom_field_data.get("gbic_model", ""),
                state=state,
                type=nbinterface.type,
                controller_tag=self.controller_tag,
            )
            self.add(_interface)

    def load_deviceroles(self):
        """Method to load Device Roles from Nautobot."""
        for nbdevicerole in Role.objects.filter(content_types=ContentType.objects.get_for_model(Device)):
            _devicerole = self.device_role(
                name=nbdevicerole.name,
                description=nbdevicerole.description,
            )
            _devicerole.model_flags = DiffSyncModelFlags.SKIP_UNMATCHED_DST
            self.add(_devicerole)

    def load_devices(self):
        """Method to load Devices from Nautobot."""
        for nbdevice in Device.objects.filter(tags__name=self.controller_tag):
            _device = self.device(
                name=nbdevice.name,
                device_type=nbdevice.device_type.model,
                device_role=nbdevice.role.name,
                serial=nbdevice.serial,
                comments=nbdevice.comments,
                site=nbdevice.location.name,
                node_id=nbdevice.custom_field_data["aci_node_id"],
                pod_id=nbdevice.custom_field_data["aci_pod_id"],
                controller_tag=self.controller_tag,
                controller_group=(
                    nbdevice.controller_managed_device_group.name if nbdevice.controller_managed_device_group else ""
                ),
            )
            self.add(_device)

    def load_ipaddresses(self):
        """Method to load IPAddress objects from Nautobot."""
        for nbipaddr in IPAddress.objects.filter(tags__name=self.controller_tag):
            if nbipaddr.interfaces.first():
                intf = nbipaddr.interfaces.first()
                device_name = intf.parent.name
                interface_name = intf.name
            else:
                device_name = None
                interface_name = None
            if nbipaddr.tenant:
                tenant_name = nbipaddr.tenant.name
            else:
                tenant_name = None
            _ipaddress = self.ip_address(
                address=str(nbipaddr.address),
                namespace=nbipaddr.parent.namespace.name,
                prefix=str(nbipaddr.parent.prefix),
                status=nbipaddr.status.name,
                description=nbipaddr.description,
                tenant=tenant_name,
                device=device_name,
                interface=interface_name,
                site=self.site,
                controller_tag=self.controller_tag,
            )
            self.add(_ipaddress)

    def load_prefixes(self):
        """Method to load Prefix objects from Nautobot."""
        for nbprefix in Prefix.objects.filter(tags__name=self.controller_tag):
            if nbprefix.vrfs.first():
                vrf = nbprefix.vrfs.first().name
                if nbprefix.vrfs.first().tenant:
                    vrf_tenant = nbprefix.vrfs.first().tenant.name
                else:
                    vrf_tenant = None
            else:
                vrf = None
                vrf_tenant = None

            _prefix = self.prefix(
                prefix=str(nbprefix.prefix),
                namespace=nbprefix.namespace.name,
                status=nbprefix.status.name,
                site=self.site,
                description=nbprefix.description,
                tenant=nbprefix.tenant.name if nbprefix.tenant else None,
                vrf=vrf,
                vrf_tenant=vrf_tenant,
                controller_tag=self.controller_tag,
            )
            self.add(_prefix)

    def load_appprofiles(self):
        """Method to load VRFs from Nautobot."""
        for nbap in ApplicationProfile.objects.filter(tags__name=self.controller_tag):  # pylint: disable=E0606
            _ap = self.aci_appprofile(
                name=nbap.name,
                tenant=nbap.tenant.name,
                description=nbap.description if not None else "",
                controller_tag=self.controller_tag,
            )
            self.add(_ap)

    def load_bridgedomains(self):
        """Method to load BDs from Nautobot."""
        for nbbd in BridgeDomain.objects.filter(tags__name=self.controller_tag):  # pylint: disable=E0606
            ip_addresses = [f"{ip.get('host')}/{ip.get('mask_length')}" for ip in list(nbbd.ip_addresses.values())]
            _bd = self.aci_bridgedomain(
                name=nbbd.name,
                vrf={
                    "name": nbbd.vrf.name,
                    "namespace": nbbd.vrf.namespace.name,
                    "vrf_tenant": nbbd.vrf.tenant.name,
                },
                ip_addresses=sorted(ip_addresses, key=hash),
                tenant=nbbd.tenant.name,
                description=nbbd.description if not None else "",
                controller_tag=self.controller_tag,
            )
            self.add(_bd)

    def load_epgs(self):
        """Method to load EPGs from Nautobot."""
        for nbepg in EPG.objects.filter(tags__name=self.controller_tag):  # pylint: disable=E0606
            _epg = self.aci_epg(
                name=nbepg.name,
                tenant=nbepg.tenant.name,
                application=nbepg.application.name,
                bridge_domain=nbepg.bridge_domain.name,
                description=nbepg.description if not None else "",
                controller_tag=self.controller_tag,
            )
            self.add(_epg)

    def load_appterminations(self):
        """Method to load EPG paths from Nautobot."""
        for nbepgpath in ApplicationTermination.objects.filter(tags__name=self.controller_tag):  # pylint: disable=E0606
            _epgpath = self.aci_apptermination(
                name=nbepgpath.name,
                epg={
                    "name": nbepgpath.epg.name,
                    "tenant": nbepgpath.epg.tenant.name,
                    "application": nbepgpath.epg.application.name,
                },
                interface={
                    "name": nbepgpath.interface.name,
                    "device": nbepgpath.interface.device.name,
                },
                vlan=nbepgpath.vlan.vid,
                description=nbepgpath.description if not None else "",
                controller_tag=self.controller_tag,
            )
            self.add(_epgpath)

    def load(self):
        """Method to load models with data from Nautbot."""
        self.load_tenants()
        self.load_vrfs()
        self.load_devicetypes()
        self.load_deviceroles()
        self.load_devices()
        self.load_interfaces()
        self.load_prefixes()
        self.load_ipaddresses()
        if HAS_NAUTOBOT_APP_CISCO_SDN:
            self.load_appprofiles()
            self.load_bridgedomains()
            self.load_epgs()
            self.load_appterminations()
