"""Unit tests for aci_models."""
from nautobot.apps.testing import APIViewTestCases
from nautobot.ipam.models import VRF
from nautobot.tenancy.models import Tenant

from aci_models import models
from aci_models.tests import fixtures


class ApplicationProfileAPIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for ACIModel."""

    model = models.ApplicationProfile
    bulk_update_data = {"description": "Test Bulk Update"}

    @classmethod
    def setUpTestData(cls):
        fixtures.create_tenants()
        fixtures.create_application_profile()

        cls.tenant_1 = Tenant.objects.get(name=fixtures.TENANT_NAMES[0])
        cls.tenant_2 = Tenant.objects.get(name=fixtures.TENANT_NAMES[1])

        cls.create_data = [
            {
                "name": "Test Model 1",
                "description": "test description",
                "tenant": cls.tenant_1.pk
            },
            {
                "name": "Test Model 2",
                "description": "test description",
                "tenant": cls.tenant_2.pk
            },
            {
                "name": "Test Model 3",
                "tenant": cls.tenant_2.pk
            },
        ]


class BridgeDomainAPIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for BridgeDomain."""

    model = models.BridgeDomain
    bulk_update_data = {"description": "Test Bulk Update"}

    @classmethod
    def setUpTestData(cls):
        fixtures.create_tenants()
        fixtures.create_ipam()
        fixtures.create_bridge_domain()

        cls.tenant_1 = Tenant.objects.get(name=fixtures.TENANT_NAMES[0])
        cls.tenant_2 = Tenant.objects.get(name=fixtures.TENANT_NAMES[1])
        cls.vrf_1 = VRF.objects.get(name=fixtures.VRF_NAMES[0])

        cls.create_data = [
            {
                "name": "Test Model 1",
                "description": "test description",
                "tenant": cls.tenant_1.pk,
                "vrf": cls.vrf_1.pk
            },
            {
                "name": "Test Model 2",
                "description": "test description",
                "tenant": cls.tenant_2.pk,
                "vrf": cls.vrf_1.pk,
            },
            {
                "name": "Test Model 3",
                "tenant": cls.tenant_2.pk,
                "vrf": cls.vrf_1.pk,
            },
        ]


class EPGAPIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for EPG."""

    model = models.EPG
    bulk_update_data = {"description": "Test Bulk Update"}

    @classmethod
    def setUpTestData(cls):
        fixtures.create_tenants()
        fixtures.create_ipam()
        fixtures.create_application_profile()
        fixtures.create_bridge_domain()
        fixtures.create_epg()

        cls.tenant_1 = Tenant.objects.get(name=fixtures.TENANT_NAMES[0])
        cls.tenant_2 = Tenant.objects.get(name=fixtures.TENANT_NAMES[1])
        cls.app_1 = models.ApplicationProfile.objects.get(name=fixtures.APP_NAMES[0])
        cls.app_2 = models.ApplicationProfile.objects.get(name=fixtures.APP_NAMES[1])
        cls.bridge_domain_1 = models.BridgeDomain.objects.get(name=fixtures.BRIDGE_DOMAINS[0])
        cls.bridge_domain_2 = models.BridgeDomain.objects.get(name=fixtures.BRIDGE_DOMAINS[1])

        cls.create_data = [
            {
                "name": "Test Model 1",
                "description": "test description",
                "tenant": cls.tenant_1.pk,
                "application": cls.app_1.pk,
                "bridge_domain": cls.bridge_domain_1.pk
            },
            {
                "name": "Test Model 2",
                "description": "test description",
                "tenant": cls.tenant_2.pk,
                "application": cls.app_2.pk,
                "bridge_domain": cls.bridge_domain_2.pk
            },
            {
                "name": "Test Model 3",
                "tenant": cls.tenant_2.pk,
                "application": cls.app_1.pk,
                "bridge_domain": cls.bridge_domain_2.pk
            },
        ]


# class ApplicationTerminationAPIViewTest(APIViewTestCases.APIViewTestCase):
#     # pylint: disable=too-many-ancestors
#     """Test the API viewsets for ApplicationTermination."""
#
#     model = models.ApplicationTermination
#     bulk_update_data = {"description": "Test Bulk Update"}
#
#     @classmethod
#     def setUpTestData(cls):
#         fixtures.create_tenants()
#         fixtures.create_ipam()
#         fixtures.create_dcim()
#         fixtures.create_application_profile()
#         fixtures.create_bridge_domain()
#         fixtures.create_epg()
#         fixtures.create_application_termination()
#
#         cls.epg_1 = models.EPG.objects.get(name=fixtures.EPG_NAMES[0])
#         cls.epg_2 = models.EPG.objects.get(name=fixtures.EPG_NAMES[1])
#         cls.epg_3 = models.EPG.objects.get(name=fixtures.EPG_NAMES[2])
#
#         from nautobot.dcim.models import Interface
#         cls.interface_4 = Interface.objects.get(name="Interface 4")
#         cls.interface_5 = Interface.objects.get(name="Interface 5")
#         cls.interface_6 = Interface.objects.get(name="Interface 6")
#
#         cls.create_data = [
#             {
#                 "name": "Test Model 1",
#                 "epg": cls.epg_1.pk,
#                 "interface": cls.interface_4.pk,
#             },
#             {
#                 "name": "Test Model 2",
#                 "epg": cls.epg_2.pk,
#                 "interface": cls.interface_5.pk,
#             },
#             {
#                 "name": "Test Model 3",
#                 "epg": cls.epg_3.pk,
#                 "interface": cls.interface_6.pk,
#             },
#         ]
