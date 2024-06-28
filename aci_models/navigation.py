"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
    NavMenuItem(
        link="plugins:aci_models:acimodel_list",
        name="Cisco ACI Models",
        permissions=["aci_models.view_acimodel"],
        buttons=(
            NavMenuAddButton(
                link="plugins:aci_models:acimodel_add",
                permissions=["aci_models.add_acimodel"],
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Apps",
        groups=(NavMenuGroup(name="Cisco ACI Models", items=tuple(items)),),
    ),
)
