"""
Boilerplate Celery Configuration
"""
###
# Libraries
###
import os

from celery import Celery
from celery.utils.log import get_task_logger
from django.conf import settings

logger = get_task_logger(__name__)

###
# Main Configuration
###
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")

app = Celery("settings")
app.config_from_object("settings.celeryconfig")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
