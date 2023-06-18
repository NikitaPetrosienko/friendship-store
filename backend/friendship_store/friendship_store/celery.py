"""
Этот код инициализирует и настраивает приложение Celery для проекта Friendship Store.

    Импортируется модуль Celery из пакета celery.
    Импортируется функция crontab из модуля celery.schedules.
    Импортируется модуль os для работы с переменными окружения.
    Переменная окружения DJANGO_SETTINGS_MODULE устанавливается в значение 'friendship_store.settings'.
    Создается экземпляр приложения Celery с именем 'friendship_store'.
    Загружается конфигурация приложения Celery из модуля настроек Django.
    Задачи автоматически обнаруживаются и регистрируются в приложении.
    Атрибут beat_schedule устанавливается для запуска задачи send_beat_email каждый первый день месяца в 9:00 утра.

Примечание: Задача send_beat_email и модуль настроек Django должны быть определены в другом месте кода.
"""

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
        'schedule': crontab(hour=9, minute=0, day_of_month=1),
    }
}
