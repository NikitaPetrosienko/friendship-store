# Generated by Django 4.2.1 on 2023-05-12 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friendship_app', '0003_alter_customer_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='User',
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]