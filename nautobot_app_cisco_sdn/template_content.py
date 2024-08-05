from django.urls import reverse

from nautobot.apps.ui import TemplateExtension


class DeviceContent(TemplateExtension):
    model = "dcim.device"

    def detail_tabs(self):
        return [
            {
                "title": "ACI App Profiles",
                "url": reverse(
                    "plugins:nautobot_app_cisco_sdn:device_aci_application_profiles",
                    kwargs={"pk": self.context["object"].pk},
                ),
            },
            {
                "title": "ACI App Terminations",
                "url": reverse(
                    "plugins:nautobot_app_cisco_sdn:device_aci_application_terminations",
                    kwargs={"pk": self.context["object"].pk},
                ),
            },
        ]


template_extensions = [DeviceContent]
