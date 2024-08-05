"""Django urlpatterns declaration for nautobot_app_cisco_sdn app."""

from django.urls import path
from nautobot.apps.urls import NautobotUIViewSetRouter

from nautobot_app_cisco_sdn import views

router = NautobotUIViewSetRouter()
router.register("application-profiles", views.ApplicationProfileUIViewSet)
router.register("bridge-domains", views.BridgeDomainUIViewSet)
router.register("epgs", views.EPGUIViewSet)
router.register("application-terminations", views.ApplicationTerminationUIViewSet)

urlpatterns = [
    path(
        "devices/<uuid:pk>/aci-application-profiles/",
        views.DeviceAciApplicationProfilesView.as_view(),
        name="device_aci_application_profiles",
    ),
    path(
        "devices/<uuid:pk>/aci-application-terminations/",
        views.DeviceAciApplicationTerminationsView.as_view(),
        name="device_aci_application_terminations",
    ),
]

urlpatterns += router.urls
