# Generated by Django 4.2.5 on 2023-12-27 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statusapp', '0003_alter_statusapp_expiration_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusapp',
            name='expiration_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 27, 11, 4, 52, 717684, tzinfo=datetime.timezone.utc)),
        ),
    ]
