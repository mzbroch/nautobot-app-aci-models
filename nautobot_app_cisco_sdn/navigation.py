"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
    NavMenuItem(
        link="plugins:nautobot_app_cisco_sdn:applicationprofile_list",
        name="Application Profiles",
        permissions=["nautobot_app_cisco_sdn.view_applicationprofile"],
        buttons=(
            NavMenuAddButton(
                link="plugins:nautobot_app_cisco_sdn:applicationprofile_add",
                permissions=["nautobot_app_cisco_sdn.add_applicationprofile"],
            ),
        ),
    ),
    NavMenuItem(
        link="plugins:nautobot_app_cisco_sdn:bridgedomain_list",
        name="Bridge Domains",
        permissions=["nautobot_app_cisco_sdn.view_bridgedomain"],
        buttons=(
            NavMenuAddButton(
                link="plugins:nautobot_app_cisco_sdn:bridgedomain_add",
                permissions=["nautobot_app_cisco_sdn.add_bridgedomain"],
            ),
        ),
    ),
    NavMenuItem(
        link="plugins:nautobot_app_cisco_sdn:epg_list",
        name="EPGs",
        permissions=["nautobot_app_cisco_sdn.view_epg"],
        buttons=(
            NavMenuAddButton(
                link="plugins:nautobot_app_cisco_sdn:epg_add",
                permissions=["nautobot_app_cisco_sdn.add_epg"],
            ),
        ),
    ),
    NavMenuItem(
        link="plugins:nautobot_app_cisco_sdn:applicationtermination_list",
        name="Application Terminations",
        permissions=["nautobot_app_cisco_sdn.view_applicationtermination"],
        buttons=(
            NavMenuAddButton(
                link="plugins:nautobot_app_cisco_sdn:applicationtermination_add",
                permissions=["nautobot_app_cisco_sdn.add_applicationtermination"],
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Apps",
        groups=(NavMenuGroup(name="Nautobot App Cisco SDN", items=tuple(items)),),
    ),
)
