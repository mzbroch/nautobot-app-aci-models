"""Test EPG forms."""
from django.test import TestCase
from nautobot.tenancy.models import Tenant

from aci_models import forms, models
from aci_models.tests import fixtures


class EPGTest(TestCase):
    """Test EPG forms."""

    @classmethod
    def setUpTestData(cls):
        """Setup test data for EPG Model."""
        fixtures.create_tenants()
        fixtures.create_ipam()
        fixtures.create_application_profile()
        fixtures.create_bridge_domain()

    def test_specifying_all_fields_success(self):
        form = forms.EPGForm(
            data={
                "name": "Development",
                "description": "Development Testing",
                "tenant": Tenant.objects.get(name=fixtures.TENANT_NAMES[0]).pk,
                "application": models.ApplicationProfile.objects.get(name=fixtures.APP_NAMES[0]).pk,
                "bridge_domain": models.BridgeDomain.objects.get(name=fixtures.BRIDGE_DOMAINS[0]).pk,
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_specifying_only_required_success(self):
        form = forms.EPGForm(
            data={
                "name": "Development",
                "tenant": Tenant.objects.get(name=fixtures.TENANT_NAMES[0]).pk,
                "application": models.ApplicationProfile.objects.get(name=fixtures.APP_NAMES[0]).pk,
                "bridge_domain": models.BridgeDomain.objects.get(name=fixtures.BRIDGE_DOMAINS[0]).pk,
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_validate_name_appprofile_is_required(self):
        form = forms.EPGForm(data={"description": "Development Testing"})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["name"])
