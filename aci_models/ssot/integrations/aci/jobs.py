"""Jobs for ACI SSoT app."""

from django.templatetags.static import static
from django.urls import reverse
from diffsync.enum import DiffSyncFlags
from nautobot.core.settings_funcs import is_truthy
from nautobot.dcim.models import Controller, Location
from nautobot.extras.jobs import BooleanVar, ChoiceVar, Job, ObjectVar
from nautobot_ssot.jobs.base import DataMapping, DataSource
from aci_models.ssot.integrations.aci.diffsync.adapters.aci import AciAdapter
from aci_models.ssot.integrations.aci.diffsync.adapters.nautobot import NautobotAdapter
from aci_models.ssot.integrations.aci.diffsync.client import AciApi
from aci_models.ssot.integrations.aci.constant import PLUGIN_CFG, HAS_ACI_MODELS
from nautobot_ssot.utils import get_username_password_https_from_secretsgroup, verify_controller_managed_device_group

name = "Cisco ACI SSoT"  # pylint: disable=invalid-name, abstract-method


class AciDataSource(DataSource, Job):  # pylint: disable=abstract-method, too-many-instance-attributes
    """ACI SSoT Data Source."""

    apic = ObjectVar(
        model=Controller,
        queryset=Controller.objects.all(),
        display_field="name",
        required=True,
        label="ACI APIC",
    )
    device_site = ObjectVar(
        model=Location,
        queryset=Location.objects.all(),
        display_field="name",
        required=False,
        label="Device(s) Location",
        help_text="New devices will be placed into this location.",
    )

    debug = BooleanVar(description="Enable for verbose debug logging.")

    class Meta:  # pylint: disable=too-few-public-methods
        """Information about the Job."""

        name = "Cisco ACI Data Source"
        data_source = "ACI"
        data_source_icon = static("nautobot_ssot_aci/aci.png")
        description = "Sync information from ACI to Nautobot"

    def __init__(self):
        """Initialize ExampleYAMLDataSource."""
        super().__init__()
        self.diffsync_flags = (self.diffsync_flags,)

    @classmethod
    def data_mappings(cls):
        """Shows mapping of models between ACI and Nautobot."""
        base_dm = (
            DataMapping("Tenant", None, "Tenant", reverse("tenancy:tenant_list")),
            DataMapping("Node", None, "Device", reverse("dcim:device_list")),
            DataMapping("Model", None, "Device Type", reverse("dcim:devicetype_list")),
            DataMapping("Controller/Leaf/Spine OOB Mgmt IP", None, "IP Address", reverse("ipam:ipaddress_list")),
            DataMapping("Subnet", None, "Prefix", reverse("ipam:prefix_list")),
            DataMapping("Interface", None, "Interface", reverse("dcim:interface_list")),
            DataMapping("VRF", None, "VRF", reverse("ipam:vrf_list")),
        )
        extension_dm = (
            DataMapping("ApplicationProfile", None, "ApplicationProfile", reverse("plugins:aci_models:applicationprofile_list")),
            DataMapping("BridgeDomain", None, "BridgeDomain", reverse("plugins:aci_models:bridgedomain_list")),
            DataMapping("EPG", None, "EPG", reverse("plugins:aci_models:epg_list")),
            DataMapping("ApplicationTermination", None, "ApplicationTermination", reverse("plugins:aci_models:applicationtermination_list")),
        )
        if HAS_ACI_MODELS:
            return base_dm + extension_dm
        return base_dm

    def load_source_adapter(self):
        """Method to instantiate and load the ACI adapter into `self.source_adapter`."""
        if not self.device_site:
            self.logger.info("Device Location is unspecified so will revert to specified Controller's Location.")
        verify_controller_managed_device_group(controller=self.apic)
        username, password = get_username_password_https_from_secretsgroup(
            group=self.apic.external_integration.secrets_group
        )
        client = AciApi(
            username=username,
            password=password,
            base_uri=self.apic.external_integration.remote_url,
            verify=self.apic.external_integration.verify_ssl,
            site=self.device_site.name if self.device_site else self.apic.location.name,
        )
        self.source_adapter = AciAdapter(
            job=self,
            sync=self.sync,
            client=client,
            tenant_prefix=self.apic.external_integration.extra_config.get("tenant_prefix"),
        )
        self.source_adapter.load()

    def load_target_adapter(self):
        """Method to instantiate and load the Nautobot adapter into `self.target_adapter`."""
        self.target_adapter = NautobotAdapter(
            job=self, sync=self.sync, site_name=self.device_site.name if self.device_site else self.apic.location.name
        )
        self.target_adapter.load()

    def run(  # pylint: disable=arguments-differ, too-many-arguments
        self, dryrun, memory_profiling, apic, device_site, debug, *args, **kwargs
    ):
        """Perform data synchronization."""
        self.apic = apic
        self.device_site = device_site
        self.debug = debug
        self.dryrun = dryrun
        self.memory_profiling = memory_profiling
        super().run(dryrun=self.dryrun, memory_profiling=self.memory_profiling, *args, **kwargs)


jobs = [AciDataSource]