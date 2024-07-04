"""Create fixtures for tests."""

from django.contrib.contenttypes.models import ContentType
from nautobot.dcim.models import Device, DeviceType, Interface, Location, LocationType, Manufacturer
from nautobot.extras.models import Role, Status
from nautobot.ipam.models import VLAN, VRF, IPAddress, Namespace, Prefix
from nautobot.tenancy.models import Tenant

from aci_models.models import EPG, ApplicationProfile, ApplicationTermination, BridgeDomain

TENANT_NAMES = [
    "Tenant One",
    "Tenant Two",
    "Tenant Three",
]

APP_NAMES = [
    "Application One",
    "Application Two",
    "Application Three",
]

APP_TERM_NAMES = [
    "First Termination",
    "Second Termination",
    "Third Termination",
]

BRIDGE_DOMAINS = [
    "Blue",
    "Red",
    "Green",
]

EPG_NAMES = [
    "Blue",
    "Red",
    "Green",
]

VRF_NAMES = ["VRF One", "VRF Two", "VRF Three"]
VLAN_NAMES = ["VLAN One", "VLAN Two", "VLAN Three"]
NAMESPACE_NAMES = ["Namespace One"]
IPS = ["10.1.1.1/24", "10.1.1.2/24",]


def create_tenants():
    """Create helper tenancy data."""
    for tenant_name in TENANT_NAMES:
        Tenant.objects.create(name=tenant_name)


def create_ipam():
    """Create helper ipam data."""
    VRF.objects.create(name=VRF_NAMES[0])
    namespace = Namespace.objects.create(name=NAMESPACE_NAMES[0])

    ipaddr_status = Status.objects.get_for_model(IPAddress).first()
    prefix_status = Status.objects.get_for_model(Prefix).first()

    Prefix.objects.create(
        prefix="10.1.1.0/24",
        namespace=namespace,
        status=prefix_status,
    )
    IPAddress.objects.create(
        address="10.1.1.1/24",
        namespace=namespace,
        status=ipaddr_status,
    )
    IPAddress.objects.create(
        address="10.1.1.2/24",
        namespace=namespace,
        status=ipaddr_status,
    )
    for i, vlan_name in enumerate(VLAN_NAMES):
        VLAN.objects.create(
            name=vlan_name,
            vid=i + 100,
            status=Status.objects.get_for_model(VLAN).first(),
        )


def create_dcim():
    """Create helper dcim data."""
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
    for i in range(6):
        Interface.objects.create(
            name=f"Interface {i+1}",
            status=Status.objects.get_for_model(Interface).first(),
            type="OTHER",
            device=device,
        )


def create_application_profile():
    """Fixture to create necessary number of Application Profile for tests."""
    ApplicationProfile.objects.create(
        name=APP_NAMES[0],
        tenant=Tenant.objects.get(name=TENANT_NAMES[0]),
        description="First Description",
    )
    ApplicationProfile.objects.create(
        name=APP_NAMES[1],
        tenant=Tenant.objects.get(name=TENANT_NAMES[1]),
        description="Second Description",
    )
    ApplicationProfile.objects.create(
        name=APP_NAMES[2],
        tenant=Tenant.objects.get(name=TENANT_NAMES[2]),
        description="Third Description",
    )


def create_bridge_domain():
    """Fixture to create necessary number of Bridge Domain for tests."""
    BridgeDomain.objects.create(
        name=BRIDGE_DOMAINS[0],
        tenant=Tenant.objects.get(name=TENANT_NAMES[0]),
        vrf=VRF.objects.get(name=VRF_NAMES[0]),
        description="Blue Domain",
    )
    BridgeDomain.objects.create(
        name=BRIDGE_DOMAINS[1],
        tenant=Tenant.objects.get(name=TENANT_NAMES[0]),
        vrf=VRF.objects.get(name=VRF_NAMES[0]),
        description="Red Domain",
    )
    BridgeDomain.objects.create(
        name=BRIDGE_DOMAINS[2],
        tenant=Tenant.objects.get(name=TENANT_NAMES[0]),
        vrf=VRF.objects.get(name=VRF_NAMES[0]),
        description="Green Domain",
    )


def create_epg():
    """Fixture to create necessary number of EPG for tests."""
    EPG.objects.create(
        name=EPG_NAMES[0],
        tenant=Tenant.objects.get(name=TENANT_NAMES[0]),
        application=ApplicationProfile.objects.get(name=APP_NAMES[0]),
        bridge_domain=BridgeDomain.objects.get(name=BRIDGE_DOMAINS[0]),
    )
    EPG.objects.create(
        name=EPG_NAMES[1],
        tenant=Tenant.objects.get(name=TENANT_NAMES[0]),
        application=ApplicationProfile.objects.get(name=APP_NAMES[1]),
        bridge_domain=BridgeDomain.objects.get(name=BRIDGE_DOMAINS[1]),
    )
    EPG.objects.create(
        name=EPG_NAMES[2],
        tenant=Tenant.objects.get(name=TENANT_NAMES[0]),
        application=ApplicationProfile.objects.get(name=APP_NAMES[2]),
        bridge_domain=BridgeDomain.objects.get(name=BRIDGE_DOMAINS[2]),
    )


def create_application_termination():
    """Fixture to create necessary number of Application Termination for tests."""
    ApplicationTermination.objects.create(
        name=APP_TERM_NAMES[0],
        epg=EPG.objects.get(name=EPG_NAMES[0]),
        interface=Interface.objects.get(name="Interface 1"),
        #vlan=VLAN.objects.get(name=VLAN_NAMES[0]),
    )
    ApplicationTermination.objects.create(
        name=APP_TERM_NAMES[1],
        epg=EPG.objects.get(name=EPG_NAMES[1]),
        interface=Interface.objects.get(name="Interface 2"),
        #vlan=VLAN.objects.get(name=VLAN_NAMES[1]),
    )
    ApplicationTermination.objects.create(
        name=APP_TERM_NAMES[2],
        epg=EPG.objects.get(name=EPG_NAMES[2]),
        interface=Interface.objects.get(name="Interface 3"),
        #vlan=VLAN.objects.get(name=VLAN_NAMES[2]),
    )
