"""Test ApplicationProfile forms."""

from django.test import TestCase
from nautobot.tenancy.models import Tenant

from aci_models import forms
from aci_models.tests import fixtures


class ApplicationProfileTest(TestCase):
    """Test ApplicationProfile forms."""

    @classmethod
    def setUpTestData(cls):
        """Setup test data for ApplicationProfile Model."""
        fixtures.create_tenants()

    def test_specifying_all_fields_success(self):
        form = forms.ApplicationProfileForm(
            data={
                "name": "Development",
                "description": "Development Testing",
                "tenant": Tenant.objects.get(name=fixtures.TENANT_NAMES[0]).pk,
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_specifying_only_required_success(self):
        form = forms.ApplicationProfileForm(
            data={
                "name": "Development",
                "tenant": Tenant.objects.get(name=fixtures.TENANT_NAMES[0]).pk,
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_validate_name_acimodel_is_required(self):
        form = forms.ApplicationProfileForm(data={"description": "Development Testing"})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["name"])
