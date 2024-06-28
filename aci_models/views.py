"""Views for aci_models."""
from nautobot.apps.views import NautobotUIViewSet

from aci_models import filters, forms, models, tables
from aci_models.api import serializers


class ACIModelUIViewSet(NautobotUIViewSet):
    """ViewSet for ACIModel views."""

    bulk_update_form_class = forms.ACIModelBulkEditForm
    filterset_class = filters.ACIModelFilterSet
    filterset_form_class = forms.ACIModelFilterForm
    form_class = forms.ACIModelForm
    lookup_field = "pk"
    queryset = models.ACIModel.objects.all()
    serializer_class = serializers.ACIModelSerializer
    table_class = tables.ACIModelTable
