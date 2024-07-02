# """Test ACIModel Filter."""
#
# from django.test import TestCase
#
# from aci_models import filters, models
# from aci_models.tests import fixtures
#
#
# class ACIModelFilterTestCase(TestCase):
#     """ACIModel Filter Test Case."""
#
#     queryset = models.ACIModel.objects.all()
#     filterset = filters.ACIModelFilterSet
#
#     @classmethod
#     def setUpTestData(cls):
#         """Setup test data for ACIModel Model."""
#         fixtures.create_acimodel()
#
#     def test_q_search_name(self):
#         """Test using Q search with name of ACIModel."""
#         params = {"q": "Test One"}
#         self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)
#
#     def test_q_invalid(self):
#         """Test using invalid Q search for ACIModel."""
#         params = {"q": "test-five"}
#         self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
