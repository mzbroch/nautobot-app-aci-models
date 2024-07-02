"""Test EPG Model."""

from django.test import TestCase

from nautobot.extras.models import Role, Status
from nautobot.ipam.models import VRF, IPAddress, Namespace, Prefix
from nautobot.tenancy.models import Tenant
from aci_models import models


class TestEPGModel(TestCase):
    """Test EPG."""

    def test_create_epg_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        tenant = Tenant.objects.create(name="Development Tenant")
        namespace = Namespace.objects.create(name="Development Namespace")
        vrf = VRF.objects.create(name="Development VRF", namespace=namespace)

        application = models.ApplicationProfile.objects.create(name="Development", tenant=tenant)

        bridge_domain = models.BridgeDomain.objects.create(
            name="Development",
            tenant=tenant,
            vrf=vrf,
        )

        instance = models.EPG.objects.create(
            name="Development EPG",
            tenant=tenant,
            application=application,
            bridge_domain=bridge_domain,
        )

        self.assertEqual(instance.name, "Development EPG")
        self.assertEqual(instance.description, "")
        self.assertEqual(instance.tenant, tenant)
        self.assertEqual(instance.application, application)
        self.assertEqual(str(instance), "Development EPG")

    def test_create_epg_all_fields_success(self):
        """Create Bridge Domain with all fields."""
        tenant = Tenant.objects.create(name="Development Tenant")
        namespace = Namespace.objects.create(name="Development Namespace")
        vrf = VRF.objects.create(name="Development VRF", namespace=namespace)

        application = models.ApplicationProfile.objects.create(name="Development", tenant=tenant)

        bridge_domain = models.BridgeDomain.objects.create(
            name="Development",
            tenant=tenant,
            vrf=vrf,
        )

        instance = models.EPG.objects.create(
            name="Development Bridge Domain",
            tenant=tenant,
            application=application,
            bridge_domain=bridge_domain,
            description="Development Bridge Domain Description",
        )

        self.assertEqual(instance.name, "Development Bridge Domain")
        self.assertEqual(instance.description, "Development Bridge Domain Description")
        self.assertEqual(instance.tenant, tenant)
        self.assertEqual(instance.application, application)
        self.assertEqual(instance.description, "Development Bridge Domain Description")
