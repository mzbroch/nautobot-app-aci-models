"""Unit tests for views."""
from nautobot.apps.testing import ViewTestCases

from aci_models import models
from aci_models.tests import fixtures


class ACIModelViewTest(ViewTestCases.PrimaryObjectViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the ACIModel views."""

    model = models.ACIModel
    bulk_edit_data = {"description": "Bulk edit views"}
    form_data = {
        "name": "Test 1",
        "description": "Initial model",
    }
    csv_data = (
        "name",
        "Test csv1",
        "Test csv2",
        "Test csv3",
    )

    @classmethod
    def setUpTestData(cls):
        fixtures.create_acimodel()
