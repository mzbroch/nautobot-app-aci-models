"""Test Bridge Domain Model."""

from django.test import TestCase
from nautobot.ipam.models import VRF, IPAddress
from nautobot.tenancy.models import Tenant

from nautobot_app_cisco_sdn import models
from nautobot_app_cisco_sdn.tests import fixtures


class TestBridgeDomainModel(TestCase):
    """Test Application Profile."""

    @classmethod
    def setUpTestData(cls):
        """Setup test data for ApplicationProfile Model."""
        fixtures.create_tenants()
        fixtures.create_ipam()

        cls.tenant = Tenant.objects.get(name=fixtures.TENANT_NAMES[0])
        cls.vrf = VRF.objects.get(name=fixtures.VRF_NAMES[0])

    def test_create_bridgedomain_only_required(self):
        """Create with only required fields, and validate null description and __str__."""

        instance = models.BridgeDomain.objects.create(
            name="Development Bridge Domain", tenant=self.tenant, vrf=self.vrf
        )

        self.assertEqual(instance.name, "Development Bridge Domain")
        self.assertEqual(instance.description, "")
        self.assertEqual(instance.tenant, self.tenant)
        self.assertEqual(str(instance), "Development Bridge Domain")

    def test_create_bridgedomain_all_fields_success(self):
        """Create BridgeDomain with all fields."""
        instance = models.BridgeDomain.objects.create(
            name="Development",
            tenant=self.tenant,
            vrf=self.vrf,
            description="Development Test",
        )
        address_1 = IPAddress.objects.get(address=fixtures.IPS[0])
        address_2 = IPAddress.objects.get(address=fixtures.IPS[1])

        instance.ip_addresses.set([address_1, address_2])

        self.assertEqual(instance.name, "Development")
        self.assertEqual(instance.description, "Development Test")
        self.assertEqual(instance.tenant, self.tenant)
        self.assertEqual(instance.vrf, self.vrf)
        self.assertTrue(address_1 in instance.ip_addresses.all())
        self.assertTrue(address_2 in instance.ip_addresses.all())
