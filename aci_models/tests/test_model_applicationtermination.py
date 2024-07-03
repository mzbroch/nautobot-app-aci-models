"""Test Application Termination Model."""

from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from nautobot.extras.models import Role, Status
from nautobot.dcim.models import Device, DeviceType, Interface, Location, LocationType, Manufacturer
from nautobot.ipam.models import VLAN, VRF, IPAddress, Namespace, Prefix
from nautobot.tenancy.models import Tenant
from aci_models import models
from aci_models.tests import fixtures


class TestApplicationTerminationModel(TestCase):
    """Test EPG."""


    @classmethod
    def setUpTestData(cls):
        """Setup test data for ApplicationProfile Model."""
        fixtures.create_tenants()
        fixtures.create_ipam()
        fixtures.create_dcim()
        fixtures.create_application_profile()
        fixtures.create_bridge_domain()
        fixtures.create_epg()
        cls.epg = models.EPG.objects.get(name=fixtures.EPG_NAMES[0])
        cls.interface = Interface.objects.first()
        cls.vlan = VLAN.objects.get(name=fixtures.VLAN_NAMES[0])


    def test_create_applicationtermination_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        instance = models.ApplicationTermination.objects.create(
            epg=self.epg,
            interface=self.interface,
        )

        self.assertEqual(instance.epg, self.epg)
        self.assertEqual(instance.interface, self.interface)
        self.assertEqual(instance.name, "")
        self.assertEqual(instance.description, "")
        self.assertEqual(str(instance), f"{self.interface.device.name}:{self.interface.name}:0")

    def test_create_epg_all_fields_success(self):
        """Create Bridge Domain with all fields."""

        instance = models.ApplicationTermination.objects.create(
            epg=self.epg,
            interface=self.interface,
            name="Development Application Termination",
            description="Development Application Description",
            vlan=self.vlan,
        )

        self.assertEqual(instance.epg, self.epg)
        self.assertEqual(instance.interface, self.interface)
        self.assertEqual(instance.name, "Development Application Termination")
        self.assertEqual(instance.description, "Development Application Description")
        self.assertEqual(str(instance), f"{self.interface.device.name}:{self.interface.name}:{self.vlan.vid}")
