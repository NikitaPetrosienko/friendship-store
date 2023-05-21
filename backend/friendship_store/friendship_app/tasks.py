from friendship_store.celery import app
from django.contrib.auth.models import User
from django.core.mail import send_mail


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
