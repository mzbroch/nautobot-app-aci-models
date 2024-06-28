"""Django urlpatterns declaration for aci_models app."""

from nautobot.apps.urls import NautobotUIViewSetRouter

from aci_models import views

router = NautobotUIViewSetRouter()
router.register("acimodel", views.ACIModelUIViewSet)

urlpatterns = router.urls
