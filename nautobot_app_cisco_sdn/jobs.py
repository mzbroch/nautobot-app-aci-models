"""Initialize Jobs for Nautobot and Cisco SDN."""
from nautobot.core.celery import register_jobs

from nautobot_app_cisco_sdn.ssot.integrations.aci.jobs import jobs as aci_jobs

jobs = aci_jobs

register_jobs(*jobs)
