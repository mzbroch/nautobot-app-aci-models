"""Test EPG Filter."""

from django.test import TestCase

from nautobot_app_cisco_sdn import filters, models
from nautobot_app_cisco_sdn.tests import fixtures


class EPGFilterTestCase(TestCase):
    """EPG Filter Test Case."""

    queryset = models.EPG.objects.all()
    filterset = filters.EPGFilterSet

    @classmethod
    def setUpTestData(cls):
        """Setup test data for EPG Model."""
        fixtures.create_tenants()
        fixtures.create_ipam()
        fixtures.create_application_profile()
        fixtures.create_bridge_domain()
        fixtures.create_epg()

    def test_q_search_name(self):
        """Test using Q search with name of EPG."""
        params = {"q": fixtures.EPG_NAMES[0]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for EPG."""
        params = {"q": "NORESULTS"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
