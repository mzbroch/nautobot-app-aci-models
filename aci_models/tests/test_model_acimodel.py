"""Test ACIModel."""

from django.test import TestCase

from aci_models import models


class TestACIModel(TestCase):
    """Test ACIModel."""

    def test_create_acimodel_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        acimodel = models.ACIModel.objects.create(name="Development")
        self.assertEqual(acimodel.name, "Development")
        self.assertEqual(acimodel.description, "")
        self.assertEqual(str(acimodel), "Development")

    def test_create_acimodel_all_fields_success(self):
        """Create ACIModel with all fields."""
        acimodel = models.ACIModel.objects.create(name="Development", description="Development Test")
        self.assertEqual(acimodel.name, "Development")
        self.assertEqual(acimodel.description, "Development Test")
