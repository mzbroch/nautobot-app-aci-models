"""Management command to bootstrap dummy data for aci model app."""

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from aci_models.tests import fixtures


class Command(BaseCommand):
    """Publish command to bootstrap dummy data."""

    def handle(self, *args, **options):
        """Publish command to bootstrap dummy data."""
        self.stdout.write("Attempting to populate dummy data.")
        try:
            fixtures.create_tenants()
            fixtures.create_ipam()
            fixtures.create_dcim()
            fixtures.create_application_profile()
            fixtures.create_bridge_domain()
            fixtures.create_epg()
            fixtures.create_application_termination()
            self.stdout.write(self.style.SUCCESS("Successfully populated dummy data!"))
        except IntegrityError:
            self.stdout.write(
                self.style.ERROR(
                    "Unable to populate data, command is not idempotent. Please validate objects do not already exist."
                )
            )
