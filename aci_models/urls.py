"""Django urlpatterns declaration for aci_models app."""

from nautobot.apps.urls import NautobotUIViewSetRouter

from aci_models import views

router = NautobotUIViewSetRouter()
router.register("application-profiles", views.ApplicationProfileUIViewSet)
router.register("bridge-domains", views.BridgeDomainUIViewSet)
router.register("epgs", views.EPGUIViewSet)
router.register("application-terminations", views.ApplicationTerminationUIViewSet)

urlpatterns = router.urls
