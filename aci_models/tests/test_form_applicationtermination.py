"""Test ApplicationTermination forms."""
from django.test import TestCase

from aci_models import models, forms
from aci_models.tests import fixtures
from nautobot.extras.models import Status
from nautobot.ipam.models import VRF, IPAddress, Namespace, Prefix
from nautobot.tenancy.models import Tenant

from nautobot.dcim.models import Interface
from nautobot.ipam.models import VLAN


class ApplicationTerminationTest(TestCase):
    """Test ApplicationTermination forms."""

    @classmethod
    def setUpTestData(cls):
        """Setup test data for ApplicationTermination Model."""
        fixtures.create_tenants()
        fixtures.create_ipam()
        fixtures.create_dcim()
        fixtures.create_application_profile()
        fixtures.create_bridge_domain()
        fixtures.create_epg()
        cls.epg = models.EPG.objects.get(name=fixtures.EPG_NAMES[0])
        cls.interface = Interface.objects.first()
        cls.vlan = VLAN.objects.get(name=fixtures.VLAN_NAMES[0])

    def test_specifying_all_fields_success(self):
        form = forms.ApplicationTerminationForm(
            data={
                "name": fixtures.EPG_NAMES[0],
                "epg": self.epg.pk,
                "interface": self.interface.pk,
                "vlan": self.vlan.pk,
                "description": "Development Testing",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_specifying_only_required_success(self):
        form = forms.ApplicationTerminationForm(
            data={
                "epg": self.epg.pk,
                "interface": self.interface.pk,
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_validate_epg_appprofile_is_required(self):
        form = forms.ApplicationTerminationForm(data={"description": "Development Testing"})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["epg"])
