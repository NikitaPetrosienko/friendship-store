from friendship_store.celery import app
from django.contrib.auth.models import User
from django.core.mail import send_mail

import datetime


@app.task
def send_beat_email():
    for user in User.objects.all():
        send_mail(
            'friendship',
            f'Здравствуйте, {user.first_name}!\n\n'
            'Мы рады представить вам новый товар, '
            'который поступил в продажу в нашем магазине!\n'
            'Чтобы ознакомится с ним переходите по ссылке:\n'
            'http://www.friendship.ru\n\n'
            'С наилучшими пожеланиями, Friendship Skate Shop.',
            'friendship@mail.ru',
            [user.email],
            fail_silently=False,
        )


@app.task
def order_notice(first_name, total_price, email):
    send_mail(
        'friendship',
        f'Здравствуйте, {first_name}!\n\n'
        f'Мы рады сообщить, что ваша покупка была успешно соверщена.\n\n'
        f'Дата покупки: {datetime.datetime.now().strftime("%d.%m.%Y")} '
        f'Сумма покупки: {total_price}\n\n'
        f'Спасибо, что выбрали наш магазин!',
        'friendship@mail.ru',
        [email],
        fail_silently=False,
    )
