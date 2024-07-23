"""Django urlpatterns declaration for aci_models app."""

from django.urls import path

from nautobot.apps.urls import NautobotUIViewSetRouter

from aci_models import views

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
]

urlpatterns += router.urls
