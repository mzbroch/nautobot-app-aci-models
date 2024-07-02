"""Test ACIModel."""

from django.test import TestCase

from nautobot.tenancy.models import Tenant
from aci_models import models


class TestApplicationProfileModel(TestCase):
    """Test Application Profile."""

    def test_create_applicationprofile_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        tenant = Tenant.objects.create(name="Development Tenant")
        app_profile_instance = models.ApplicationProfile.objects.create(name="Development", tenant=tenant)
        self.assertEqual(app_profile_instance.name, "Development")
        self.assertEqual(app_profile_instance.description, "")
        self.assertEqual(app_profile_instance.tenant, tenant)
        self.assertEqual(str(app_profile_instance), "Development")

    def test_create_applicationprofile_all_fields_success(self):
        """Create ApplicationProfile with all fields."""
        tenant = Tenant.objects.create(name="Development Tenant")
        app_profile_instance = models.ApplicationProfile.objects.create(
            name="Development",
            tenant=tenant,
            description="Development Test",
        )
        self.assertEqual(app_profile_instance.name, "Development")
        self.assertEqual(app_profile_instance.description, "Development Test")
        self.assertEqual(app_profile_instance.tenant, tenant)
