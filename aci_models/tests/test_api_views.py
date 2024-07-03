"""Unit tests for aci_models."""
from nautobot.apps.testing import APIViewTestCases

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
                "tenant": cls.tenant_2.pk
            },
        ]
