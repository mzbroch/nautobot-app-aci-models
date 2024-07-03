"""Unit tests for aci_models."""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from nautobot.users.models import Token
from rest_framework import status
from rest_framework.test import APIClient

from aci_models.tests import fixtures

User = get_user_model()


class ApplicationProfileAPITest(TestCase):
    """Test the Application Profile ACI Models API."""

    def setUp(self):
        """Create a superuser and token for API calls."""
        self.user = User.objects.create(username="testuser", is_superuser=True)
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        fixtures.create_tenants()
        fixtures.create_application_profile()

    def test_application_profile_list(self):
        """Verify that Application Profiles can be listed."""
        url = reverse("plugins-api:aci_models-api:applicationprofile-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], len(fixtures.APP_NAMES))


class BridgeDomainAPITest(TestCase):
    """Test the Bridge Domain ACI Models API."""

    def setUp(self):
        """Create a superuser and token for API calls."""
        self.user = User.objects.create(username="testuser", is_superuser=True)
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        fixtures.create_tenants()
        fixtures.create_ipam()
        fixtures.create_bridge_domain()

    def test_application_profile_list(self):
        """Verify that Application Profiles can be listed."""
        url = reverse("plugins-api:aci_models-api:bridgedomain-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], len(fixtures.APP_NAMES))


class EPGAPITest(TestCase):
    """Test the EPG ACI Models API."""

    def setUp(self):
        """Create a superuser and token for API calls."""
        self.user = User.objects.create(username="testuser", is_superuser=True)
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        fixtures.create_tenants()
        fixtures.create_ipam()
        fixtures.create_application_profile()
        fixtures.create_bridge_domain()
        fixtures.create_epg()

    def test_application_profile_list(self):
        """Verify that Application Profiles can be listed."""
        url = reverse("plugins-api:aci_models-api:epg-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], len(fixtures.APP_NAMES))


class ApplicationTerminationAPITest(TestCase):
    """Test the ApplicationTermination ACI Models API."""

    def setUp(self):
        """Create a superuser and token for API calls."""
        self.user = User.objects.create(username="testuser", is_superuser=True)
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        fixtures.create_tenants()
        fixtures.create_ipam()
        fixtures.create_dcim()
        fixtures.create_application_profile()
        fixtures.create_bridge_domain()
        fixtures.create_epg()
        fixtures.create_application_termination()

    def test_application_profile_list(self):
        """Verify that Application Profiles can be listed."""
        url = reverse("plugins-api:aci_models-api:applicationtermination-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], len(fixtures.APP_NAMES))
