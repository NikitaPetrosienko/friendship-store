import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'friendship_store.settings')

app = Celery('friendship_store')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-spam-every-1-minute': {
        'task': 'friendship_app.tasks.send_beat_email',
        'schedule': crontab(minute='*/1')
    }
}