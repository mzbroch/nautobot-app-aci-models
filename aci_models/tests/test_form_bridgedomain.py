"""Test BridgeDomain forms."""

from django.test import TestCase
from nautobot.ipam.models import VRF, IPAddress
from nautobot.tenancy.models import Tenant

from aci_models import forms
from aci_models.tests import fixtures


class BridgeDomainTest(TestCase):
    """Test BridgeDomain forms."""

    @classmethod
    def setUpTestData(cls):
        """Setup test data for BridgeDomain Model."""
        fixtures.create_tenants()
        fixtures.create_ipam()

    def test_specifying_all_fields_success(self):
        form = forms.BridgeDomainForm(
            data={
                "name": "Development",
                "description": "Development Testing",
                "tenant": Tenant.objects.get(name=fixtures.TENANT_NAMES[0]).pk,
                "vrf": VRF.objects.get(name=fixtures.VRF_NAMES[0]).pk,
                "ip_addresses": [
                    IPAddress.objects.get(address=fixtures.IPS[0]).pk,
                    IPAddress.objects.get(address=fixtures.IPS[1]).pk,
                ],
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_specifying_only_required_success(self):
        form = forms.BridgeDomainForm(
            data={
                "name": "Development",
                "tenant": Tenant.objects.get(name=fixtures.TENANT_NAMES[0]).pk,
                "vrf": VRF.objects.get(name=fixtures.VRF_NAMES[0]).pk,
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_validate_name_appprofile_is_required(self):
        form = forms.BridgeDomainForm(data={"description": "Development Testing"})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["name"])
