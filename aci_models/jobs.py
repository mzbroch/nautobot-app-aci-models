from nautobot.core.celery import register_jobs

from aci_models.ssot.integrations.aci.jobs import jobs as aci_jobs

jobs = aci_jobs

register_jobs(*jobs)
