"""
Boilerplate Celery Configuration File
"""
###
# Libraries
###
from django.conf import settings

###
# Configs
###
task_default_queue = settings.CELERY_DEFAULT_QUEUE
broker_url = settings.CELERY_URL
accept_content = ['json']
task_serializer = 'json'
result_serializer = 'json'
timezone = 'America/New_York'

if settings.ENVIRONMENT == 'test':
    task_always_eager = True
