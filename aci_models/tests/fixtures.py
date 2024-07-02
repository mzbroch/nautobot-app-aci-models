"""Create fixtures for tests."""
from nautobot.tenancy.models import Tenant
from aci_models.models import ApplicationProfile, ApplicationTermination, BridgeDomain, EPG

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


def create_tenant():
    Tenant.objects.create(name=TENANT_NAMES[0])
    Tenant.objects.create(name=TENANT_NAMES[1])


def create_application_profile():
    """Fixture to create necessary number of Application Profile for tests."""

    create_tenant()

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
