from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet_rh.settings')

app = Celery('projet_rh')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

from celery.schedules import crontab

app.conf.beat_schedule = {
    'send-turnover-alerts-every-morning': {
        'task': 'gestion.tasks.send_turnover_alerts_task',
        'schedule': crontab(hour=8, minute=0),  # Tous les jours à 8h du matin
    },
}
