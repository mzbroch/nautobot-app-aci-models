"""Django API urlpatterns declaration for aci_models app."""

from nautobot.apps.api import OrderedDefaultRouter

from aci_models.api import views

router = OrderedDefaultRouter()

router.register("application-profiles", views.ApplicationProfileViewSet)
router.register("bridge-domains", views.BridgeDomainViewSet)
router.register("epgs", views.EPGViewSet)
router.register("application-terminations", views.ApplicationTerminationViewSet)

urlpatterns = router.urls
