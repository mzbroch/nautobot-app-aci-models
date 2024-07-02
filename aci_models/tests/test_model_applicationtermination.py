"""Test Application Termination Model."""

from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from nautobot.extras.models import Role, Status
from nautobot.dcim.models import Device, DeviceType, Interface, Location, LocationType, Manufacturer
from nautobot.ipam.models import VLAN, VRF, IPAddress, Namespace, Prefix
from nautobot.tenancy.models import Tenant
from aci_models import models


class TestApplicationTerminationModel(TestCase):
    """Test EPG."""

    def test_create_applicationtermination_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        tenant = Tenant.objects.create(name="Development Tenant")
        namespace = Namespace.objects.create(name="Development Namespace")
        vrf = VRF.objects.create(name="Development VRF", namespace=namespace)

        application = models.ApplicationProfile.objects.create(name="Development", tenant=tenant)

        bridge_domain = models.BridgeDomain.objects.create(
            name="Development",
            tenant=tenant,
            vrf=vrf,
        )

        epg = models.EPG.objects.create(
            name="Development EPG",
            tenant=tenant,
            application=application,
            bridge_domain=bridge_domain,
        )

        location_type = LocationType.objects.create(name="Location Type")
        location_type.content_types.add(ContentType.objects.get_for_model(Device))
        location = Location.objects.create(
            location_type=location_type,
            name="Development Location",
            status=Status.objects.get_for_model(Location).first()
        )

        manufacturer = Manufacturer.objects.create(name="Development Manufacturer")
        device_type = DeviceType.objects.create(manufacturer=manufacturer, model="Device Type 1")
        device_role = Role.objects.create(name="Device Role")
        device_role.content_types.add(ContentType.objects.get_for_model(Device))
        device_status = Status.objects.get_for_model(Device).first()

        device = Device.objects.create(
            device_type=device_type,
            name="Device 1",
            location=location,
            role=device_role,
            status=device_status,
        )

        interface = Interface.objects.create(
            name="Interface 1",
            status=Status.objects.get_for_model(Interface).first(),
            type="OTHER",
            device=device,
        )

        instance = models.ApplicationTermination.objects.create(
            epg=epg,
            interface=interface,
        )

        self.assertEqual(instance.epg, epg)
        self.assertEqual(instance.interface, interface)
        self.assertEqual(instance.name, "")
        self.assertEqual(instance.description, "")
        self.assertEqual(str(instance), "Device 1:Interface 1:0")

    def test_create_epg_all_fields_success(self):
        """Create Bridge Domain with all fields."""
        tenant = Tenant.objects.create(name="Development Tenant")
        namespace = Namespace.objects.create(name="Development Namespace")
        vrf = VRF.objects.create(name="Development VRF", namespace=namespace)

        application = models.ApplicationProfile.objects.create(name="Development", tenant=tenant)

        bridge_domain = models.BridgeDomain.objects.create(
            name="Development",
            tenant=tenant,
            vrf=vrf,
        )

        epg = models.EPG.objects.create(
            name="Development EPG",
            tenant=tenant,
            application=application,
            bridge_domain=bridge_domain,
        )

        location_type = LocationType.objects.create(name="Location Type")
        location_type.content_types.add(ContentType.objects.get_for_model(Device))
        location = Location.objects.create(
            location_type=location_type,
            name="Development Location",
            status=Status.objects.get_for_model(Location).first()
        )

        manufacturer = Manufacturer.objects.create(name="Development Manufacturer")
        device_type = DeviceType.objects.create(manufacturer=manufacturer, model="Device Type 1")
        device_role = Role.objects.create(name="Device Role")
        device_role.content_types.add(ContentType.objects.get_for_model(Device))
        device_status = Status.objects.get_for_model(Device).first()

        device = Device.objects.create(
            device_type=device_type,
            name="Device 1",
            location=location,
            role=device_role,
            status=device_status,
        )

        vlan = VLAN.objects.create(
            name="VLAN 1",
            vid=123,
            status=Status.objects.get_for_model(VLAN).first(),
        )

        interface = Interface.objects.create(
            name="Interface 1",
            status=Status.objects.get_for_model(Interface).first(),
            type="OTHER",
            device=device,
        )

        instance = models.ApplicationTermination.objects.create(
            epg=epg,
            interface=interface,
            name="Development Application Termination",
            description="Development Application Description",
            vlan=vlan,
        )

        self.assertEqual(instance.epg, epg)
        self.assertEqual(instance.interface, interface)
        self.assertEqual(instance.name, "Development Application Termination")
        self.assertEqual(instance.description, "Development Application Description")
        self.assertEqual(str(instance), "Device 1:Interface 1:123")
