# Generated by Django 4.0 on 2022-01-04 14:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_reservations_rese_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='rese_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 4, 14, 59, 4, 359432, tzinfo=utc)),
        ),
    ]
