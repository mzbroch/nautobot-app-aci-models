"""Django API urlpatterns declaration for aci_models app."""

from nautobot.apps.api import OrderedDefaultRouter

from aci_models.api import views

router = OrderedDefaultRouter()

router.register("application-profile", views.ApplicationProfileViewSet)
router.register("bridge-domain", views.BridgeDomainViewSet)
router.register("epg", views.EPGViewSet)
router.register("application-termination", views.ApplicationTerminationViewSet)

urlpatterns = router.urls
