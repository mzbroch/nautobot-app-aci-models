"""Django urlpatterns declaration for aci_models app."""

from nautobot.apps.urls import NautobotUIViewSetRouter

from aci_models import views

router = NautobotUIViewSetRouter()
router.register("application-profile", views.ApplicationProfileUIViewSet)
router.register("bridge-domain", views.BridgeDomainUIViewSet)
router.register("epg", views.EPGUIViewSet)
router.register("application-termination", views.ApplicationTerminationUIViewSet)

urlpatterns = router.urls
