"""Views for aci_models."""

from nautobot.apps.views import NautobotUIViewSet

from aci_models import filters, forms, models, tables
from aci_models.api import serializers


class ApplicationProfileUIViewSet(NautobotUIViewSet):
    """ViewSet for ApplicationProfile views."""

    bulk_update_form_class = forms.ApplicationProfileBulkEditForm
    filterset_class = filters.ApplicationProfileFilterSet
    filterset_form_class = forms.ApplicationProfileFilterForm
    form_class = forms.ApplicationProfileForm
    lookup_field = "pk"
    queryset = models.ApplicationProfile.objects.all()
    serializer_class = serializers.ApplicationProfileSerializer
    table_class = tables.ApplicationProfileTable


class BridgeDomainUIViewSet(NautobotUIViewSet):
    """ViewSet for BridgeDomain views."""

    bulk_update_form_class = forms.BridgeDomainBulkEditForm
    filterset_class = filters.BridgeDomainFilterSet
    filterset_form_class = forms.BridgeDomainFilterForm
    form_class = forms.BridgeDomainForm
    lookup_field = "pk"
    queryset = models.BridgeDomain.objects.all()
    serializer_class = serializers.BridgeDomainSerializer
    table_class = tables.BridgeDomainTable


class EPGUIViewSet(NautobotUIViewSet):
    """ViewSet for EPG views."""

    bulk_update_form_class = forms.EPGBulkEditForm
    filterset_class = filters.EPGFilterSet
    filterset_form_class = forms.EPGFilterForm
    form_class = forms.EPGForm
    lookup_field = "pk"
    queryset = models.EPG.objects.all()
    serializer_class = serializers.EPGSerializer
    table_class = tables.EPGTable


class ApplicationTerminationUIViewSet(NautobotUIViewSet):
    """ViewSet for ACIModel views."""

    bulk_update_form_class = forms.ApplicationTerminationBulkEditForm
    filterset_class = filters.ApplicationTerminationFilterSet
    filterset_form_class = forms.ApplicationTerminationFilterForm
    form_class = forms.ApplicationTerminationForm
    lookup_field = "pk"
    queryset = models.ApplicationTermination.objects.all()
    serializer_class = serializers.ApplicationTerminationSerializer
    table_class = tables.ApplicationTerminationTable
