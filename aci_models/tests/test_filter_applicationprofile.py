"""Test ApplicationProfile Filter."""

from django.test import TestCase

from aci_models import filters, models
from aci_models.tests import fixtures


class ApplicationProfileFilterTestCase(TestCase):
    """ApplicationProfile Filter Test Case."""

    queryset = models.ApplicationProfile.objects.all()
    filterset = filters.ApplicationProfileFilterSet

    @classmethod
    def setUpTestData(cls):
        """Setup test data for ApplicationProfile Model."""
        fixtures.create_tenants()
        fixtures.create_application_profile()

    def test_q_search_name(self):
        """Test using Q search with name of ApplicationProfile."""
        params = {"q": fixtures.APP_NAMES[0]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for ApplicationProfile."""
        params = {"q": "NORESULTS"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
