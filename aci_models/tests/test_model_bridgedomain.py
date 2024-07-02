"""Test Bridge Domain Model."""

from django.test import TestCase

from nautobot.extras.models import Status
from nautobot.ipam.models import VRF, IPAddress, Namespace, Prefix
from nautobot.tenancy.models import Tenant
from aci_models import models


class TestBridgeDomainModel(TestCase):
    """Test Application Profile."""

    def test_create_bridgedomain_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        tenant = Tenant.objects.create(name="Development Tenant")
        namespace = Namespace.objects.create(name="Development Namespace")
        vrf = VRF.objects.create(name="Development VRF", namespace=namespace)

        instance = models.BridgeDomain.objects.create(
            name="Development Bridge Domain",
            tenant=tenant,
            vrf=vrf,
        )

        self.assertEqual(instance.name, "Development Bridge Domain")
        self.assertEqual(instance.description, "")
        self.assertEqual(instance.tenant, tenant)
        self.assertEqual(str(instance), "Development Bridge Domain")

    def test_create_bridgedomain_all_fields_success(self):
        """Create BridgeDomain with all fields."""
        tenant = Tenant.objects.create(name="Development Tenant")
        vrf = VRF.objects.create(name="Development VRF")

        ipaddr_status = Status.objects.get_for_model(IPAddress).first()
        prefix_status = Status.objects.get_for_model(Prefix).first()
        namespace = Namespace.objects.create(name="Development Namespace")

        Prefix.objects.create(prefix="10.1.1.0/24", namespace=namespace, status=prefix_status)
        address_1 = IPAddress.objects.create(address="10.1.1.1/24", namespace=namespace, status=ipaddr_status)
        address_2 = IPAddress.objects.create(address="10.1.1.2/24", namespace=namespace, status=ipaddr_status)

        instance = models.BridgeDomain.objects.create(
            name="Development",
            tenant=tenant,
            vrf=vrf,
            description="Development Test",
        )
        instance.ip_addresses.set([address_1, address_2])

        self.assertEqual(instance.name, "Development")
        self.assertEqual(instance.description, "Development Test")
        self.assertEqual(instance.tenant, tenant)
        self.assertEqual(instance.vrf, vrf)
        self.assertTrue(address_1 in instance.ip_addresses.all())
        self.assertTrue(address_2 in instance.ip_addresses.all())
