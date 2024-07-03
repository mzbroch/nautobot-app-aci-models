"""Unit tests for aci_models."""
from nautobot.apps.testing import APIViewTestCases

from nautobot.ipam.models import VRF
from nautobot.tenancy.models import Tenant

from aci_models import models
from aci_models.tests import fixtures


class ApplicationProfileAPIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for ACIModel."""

    model = models.ApplicationProfile
    bulk_update_data = {"description": "Test Bulk Update"}

    @classmethod
    def setUpTestData(cls):
        fixtures.create_tenants()
        fixtures.create_application_profile()

        cls.tenant_1 = Tenant.objects.get(name=fixtures.TENANT_NAMES[0])
        cls.tenant_2 = Tenant.objects.get(name=fixtures.TENANT_NAMES[1])

        cls.create_data = [
            {
                "name": "Test Model 1",
                "description": "test description",
                "tenant": cls.tenant_1.pk
            },
            {
                "name": "Test Model 2",
                "description": "test description",
                "tenant": cls.tenant_2.pk
            },
            {
                "name": "Test Model 3",
                "tenant": cls.tenant_2.pk
            },
        ]


class BridgeDomainAPIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for BridgeDomain."""

    model = models.BridgeDomain
    bulk_update_data = {"description": "Test Bulk Update"}

    @classmethod
    def setUpTestData(cls):
        fixtures.create_tenants()
        fixtures.create_ipam()
        fixtures.create_bridge_domain()

        cls.tenant_1 = Tenant.objects.get(name=fixtures.TENANT_NAMES[0])
        cls.tenant_2 = Tenant.objects.get(name=fixtures.TENANT_NAMES[1])
        cls.vrf_1 = VRF.objects.get(name=fixtures.VRF_NAMES[0])

        cls.create_data = [
            {
                "name": "Test Model 1",
                "description": "test description",
                "tenant": cls.tenant_1.pk,
                "vrf": cls.vrf_1.pk
            },
            {
                "name": "Test Model 2",
                "description": "test description",
                "tenant": cls.tenant_2.pk,
                "vrf": cls.vrf_1.pk,
            },
            {
                "name": "Test Model 3",
                "tenant": cls.tenant_2.pk,
                "vrf": cls.vrf_1.pk,
            },
        ]
