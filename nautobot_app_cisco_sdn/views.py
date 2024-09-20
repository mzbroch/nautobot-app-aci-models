"""Views for nautobot_app_cisco_sdn."""

from nautobot.apps.views import NautobotUIViewSet
from nautobot.core.views import generic
from nautobot.dcim.models import Device

from nautobot_app_cisco_sdn import filters, forms, models, tables
from nautobot_app_cisco_sdn.api import serializers


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


class DeviceAciApplicationProfilesView(generic.ObjectView):
    """_summary_.

    Args:
        generic (_type_): _description_

    Returns:
        _type_: _description_
    """
    queryset = Device.objects.all()
    template_name = "device_aci_application_profiles.html"

    def get_extra_context(self, request, instance):
        """_summary_.

        Args:
            request (_type_): _description_
            instance (_type_): _description_

        Returns:
            _type_: _description_
        """
        terminations = models.ApplicationTermination.objects.filter(interface__device=instance)
        epgs = models.EPG.objects.filter(aci_appterminations__in=terminations)
        application_profiles = models.ApplicationProfile.objects.filter(
            aci_epgs__in=epgs,
        )
        app_table = tables.ApplicationProfileTable(data=application_profiles, user=request.user, orderable=False)

        return {
            "app_table": app_table,
            "active_tab": request.GET.get("tab"),
        }


class DeviceAciApplicationTerminationsView(generic.ObjectView):
    """_summary_.

    Args:
        generic (_type_): _description_

    Returns:
        _type_: _description_
    """
    queryset = Device.objects.all()
    template_name = "device_aci_application_terminations.html"

    def get_extra_context(self, request, instance):
        """_summary_.

        Args:
            request (_type_): _description_
            instance (_type_): _description_

        Returns:
            _type_: _description_
        """
        terminations = models.ApplicationTermination.objects.filter(interface__device=instance).order_by("interface__name")
        terminations_table = tables.ApplicationTerminationTable(data=terminations, user=request.user, orderable=True)
        terminations_table.columns.hide("device")
        terminations_table.sequence = (
            "interface",
            "epg__application__name",
            "vlan",
        )

        return {
            "terminations_table": terminations_table,
            "active_tab": request.GET.get("tab"),
        }
