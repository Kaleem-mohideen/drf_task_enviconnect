# Generated by Django 3.2.3 on 2023-08-25 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfDataAvailabilityApp', '0002_alter_datapoint_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 25, 16, 13, 1, 316322), null=True),
        ),
    ]