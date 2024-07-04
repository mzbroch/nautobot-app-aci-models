"""Test Application Profile Model."""

from django.test import TestCase
from nautobot.tenancy.models import Tenant

from aci_models import models
from aci_models.tests import fixtures


class TestApplicationProfileModel(TestCase):
    """Test Application Profile."""

    @classmethod
    def setUpTestData(cls):
        """Setup test data for ApplicationProfile Model."""
        fixtures.create_tenants()
        cls.tenant = Tenant.objects.get(name=fixtures.TENANT_NAMES[0])

    def test_create_applicationprofile_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        app_profile_instance = models.ApplicationProfile.objects.create(
            name="Development",
            tenant=self.tenant,
        )
        self.assertEqual(app_profile_instance.name, "Development")
        self.assertEqual(app_profile_instance.description, "")
        self.assertEqual(app_profile_instance.tenant, self.tenant)
        self.assertEqual(str(app_profile_instance), "Development")

    def test_create_applicationprofile_all_fields_success(self):
        """Create ApplicationProfile with all fields."""
        app_profile_instance = models.ApplicationProfile.objects.create(
            name="Development",
            tenant=self.tenant,
            description="Development Test",
        )
        self.assertEqual(app_profile_instance.name, "Development")
        self.assertEqual(app_profile_instance.description, "Development Test")
        self.assertEqual(app_profile_instance.tenant, self.tenant)
