# Generated by Django 3.2.3 on 2023-08-25 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfDataAvailabilityApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 25, 16, 4, 12, 183978), null=True),
        ),
    ]
