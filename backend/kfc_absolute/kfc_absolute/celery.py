import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kfc_absolute.settings')

app = Celery('kfc_absolute')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()