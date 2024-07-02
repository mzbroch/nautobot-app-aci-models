# """Unit tests for aci_models."""
# from nautobot.apps.testing import APIViewTestCases
#
# from aci_models import models
# from aci_models.tests import fixtures
#
#
# class ACIModelAPIViewTest(APIViewTestCases.APIViewTestCase):
#     # pylint: disable=too-many-ancestors
#     """Test the API viewsets for ACIModel."""
#
#     model = models.ACIModel
#     create_data = [
#         {
#             "name": "Test Model 1",
#             "description": "test description",
#         },
#         {
#             "name": "Test Model 2",
#         },
#     ]
#     bulk_update_data = {"description": "Test Bulk Update"}
#
#     @classmethod
#     def setUpTestData(cls):
#         fixtures.create_acimodel()
