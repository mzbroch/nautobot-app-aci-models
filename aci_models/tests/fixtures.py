"""Create fixtures for tests."""
from nautobot.tenancy.models import Tenant
from aci_models.models import ApplicationProfile, ApplicationTermination, BridgeDomain, EPG
from nautobot.extras.models import Status
from nautobot.ipam.models import VRF, IPAddress, Namespace, Prefix
from nautobot.tenancy.models import Tenant

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

BRIDGE_DOMAINS = [
    "Blue",
    "Red",
    "Green",
]

VRF_NAMES = ["VRF One", "VRF Two", "VRF Three"]
NAMESPACE_NAMES = ["Namespace One"]
IPS = ["10.1.1.1/24", "10.1.1.2/24",]


def create_tenants():
    for tenant_name in TENANT_NAMES:
        Tenant.objects.create(name=tenant_name)


def create_ipam():
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

    # instance.ip_addresses.set([address_1, address_2])
