"""Test BridgeDomain Filter."""

from django.test import TestCase

from nautobot_app_cisco_sdn import filters, models
from nautobot_app_cisco_sdn.tests import fixtures


class BridgeDomainFilterTestCase(TestCase):
    """BridgeDomain Filter Test Case."""

    queryset = models.BridgeDomain.objects.all()
    filterset = filters.BridgeDomainFilterSet

    @classmethod
    def setUpTestData(cls):
        """Setup test data for BridgeDomain Model."""
        fixtures.create_tenants()
        fixtures.create_ipam()
        fixtures.create_bridge_domain()

    def test_q_search_name(self):
        """Test using Q search with name of BridgeDomain."""
        params = {"q": fixtures.BRIDGE_DOMAINS[0]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for BridgeDomain."""
        params = {"q": "NORESULTS"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
