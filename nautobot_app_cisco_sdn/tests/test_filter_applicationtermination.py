"""Test ApplicationTermination Filter."""

from django.test import TestCase

from nautobot_app_cisco_sdn import filters, models
from nautobot_app_cisco_sdn.tests import fixtures


class ApplicationTerminationFilterTestCase(TestCase):
    """ApplicationTermination Filter Test Case."""

    queryset = models.ApplicationTermination.objects.all()
    filterset = filters.ApplicationTerminationFilterSet

    @classmethod
    def setUpTestData(cls):
        """Setup test data for ApplicationTermination Model."""
        fixtures.create_tenants()
        fixtures.create_ipam()
        fixtures.create_dcim()
        fixtures.create_application_profile()
        fixtures.create_bridge_domain()
        fixtures.create_epg()
        fixtures.create_application_termination()

    def test_q_search_name(self):
        """Test using Q search with name of ApplicationTermination."""
        params = {"q": fixtures.APP_TERM_NAMES[0]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for ApplicationTermination."""
        params = {"q": "NORESULTS"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
