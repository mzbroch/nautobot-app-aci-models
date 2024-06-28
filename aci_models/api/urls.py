"""Django API urlpatterns declaration for aci_models app."""

from nautobot.apps.api import OrderedDefaultRouter

from aci_models.api import views

router = OrderedDefaultRouter()
# add the name of your api endpoint, usually hyphenated model name in plural, e.g. "my-model-classes"
router.register("acimodel", views.ACIModelViewSet)

urlpatterns = router.urls
