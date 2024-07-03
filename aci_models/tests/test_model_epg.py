"""Test EPG Model."""

from django.test import TestCase

from nautobot.extras.models import Role, Status
from nautobot.ipam.models import VRF, IPAddress, Namespace, Prefix
from nautobot.tenancy.models import Tenant
from aci_models import models
from aci_models.tests import fixtures


class TestEPGModel(TestCase):
    """Test EPG."""

    @classmethod
    def setUpTestData(cls):
        """Setup test data for ApplicationProfile Model."""
        fixtures.create_tenants()
        fixtures.create_ipam()
        fixtures.create_application_profile()
        fixtures.create_bridge_domain()

        cls.tenant = Tenant.objects.get(name=fixtures.TENANT_NAMES[0])
        cls.vrf = VRF.objects.get(name=fixtures.VRF_NAMES[0])
        cls.application = models.ApplicationProfile.objects.get(name=fixtures.APP_NAMES[0])
        cls.bridge_domain = models.BridgeDomain.objects.get(name=fixtures.BRIDGE_DOMAINS[0])

    def test_create_epg_only_required(self):
        instance = models.EPG.objects.create(
            name="Development EPG",
            tenant=self.tenant,
            application=self.application,
            bridge_domain=self.bridge_domain,
        )

        self.assertEqual(instance.name, "Development EPG")
        self.assertEqual(instance.description, "")
        self.assertEqual(instance.tenant, self.tenant)
        self.assertEqual(instance.application, self.application)
        self.assertEqual(str(instance), "Development EPG")

    def test_create_epg_all_fields_success(self):
        """Create Bridge Domain with all fields."""
        instance = models.EPG.objects.create(
            name="Development Bridge Domain",
            tenant=self.tenant,
            application=self.application,
            bridge_domain=self.bridge_domain,
            description="Development Bridge Domain Description",
        )

        self.assertEqual(instance.name, "Development Bridge Domain")
        self.assertEqual(instance.description, "Development Bridge Domain Description")
        self.assertEqual(instance.tenant, self.tenant)
        self.assertEqual(instance.application, self.application)
        self.assertEqual(instance.description, "Development Bridge Domain Description")
