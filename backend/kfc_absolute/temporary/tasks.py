from celery import shared_task
from django.utils import timezone

from .models import Temporary


@shared_task
def delete_record(record_id):
    record = Temporary.objects.get(pk=record_id)
    if record.date_add < timezone.now():
        record.delete()
