"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
    NavMenuItem(
        link="plugins:aci_models:applicationprofile_list",
        name="Application Profiles",
        permissions=["aci_models.view_applicationprofile"],
        buttons=(
            NavMenuAddButton(
                link="plugins:aci_models:applicationprofile_add",
                permissions=["aci_models.add_applicationprofile"],
            ),
        ),
    ),
    NavMenuItem(
        link="plugins:aci_models:bridgedomain_list",
        name="Bridge Domains",
        permissions=["aci_models.view_bridgedomain"],
        buttons=(
            NavMenuAddButton(
                link="plugins:aci_models:bridgedomain_add",
                permissions=["aci_models.add_bridgedomain"],
            ),
        ),
    ),
    NavMenuItem(
        link="plugins:aci_models:epg_list",
        name="EPGs",
        permissions=["aci_models.view_epg"],
        buttons=(
            NavMenuAddButton(
                link="plugins:aci_models:epg_add",
                permissions=["aci_models.add_epg"],
            ),
        ),
    ),
    NavMenuItem(
        link="plugins:aci_models:applicationtermination_list",
        name="Application Terminations",
        permissions=["aci_models.view_applicationtermination"],
        buttons=(
            NavMenuAddButton(
                link="plugins:aci_models:applicationtermination_add",
                permissions=["aci_models.add_applicationtermination"],
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
