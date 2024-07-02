# """Test acimodel forms."""
# from django.test import TestCase
#
# from aci_models import forms
#
#
# class ACIModelTest(TestCase):
#     """Test ACIModel forms."""
#
#     def test_specifying_all_fields_success(self):
#         form = forms.ACIModelForm(
#             data={
#                 "name": "Development",
#                 "description": "Development Testing",
#             }
#         )
#         self.assertTrue(form.is_valid())
#         self.assertTrue(form.save())
#
#     def test_specifying_only_required_success(self):
#         form = forms.ACIModelForm(
#             data={
#                 "name": "Development",
#             }
#         )
#         self.assertTrue(form.is_valid())
#         self.assertTrue(form.save())
#
#     def test_validate_name_acimodel_is_required(self):
#         form = forms.ACIModelForm(data={"description": "Development Testing"})
#         self.assertFalse(form.is_valid())
#         self.assertIn("This field is required.", form.errors["name"])
