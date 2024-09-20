"""Django API urlpatterns declaration for nautobot_app_cisco_sdn app."""

from nautobot.apps.api import OrderedDefaultRouter

from nautobot_app_cisco_sdn.api import views

router = OrderedDefaultRouter()

router.register("application-profiles", views.ApplicationProfileViewSet)
router.register("bridge-domains", views.BridgeDomainViewSet)
router.register("epgs", views.EPGViewSet)
router.register("application-terminations", views.ApplicationTerminationViewSet)

urlpatterns = router.urls
