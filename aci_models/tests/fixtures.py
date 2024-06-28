"""Create fixtures for tests."""
from aci_models.models import ACIModel


def create_acimodel():
    """Fixture to create necessary number of ACIModel for tests."""
    ACIModel.objects.create(name="Test One")
    ACIModel.objects.create(name="Test Two")
    ACIModel.objects.create(name="Test Three")
