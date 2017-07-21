# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_expire_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='priority',
            field=models.CharField(default=b'Normal', max_length=50, choices=[(1, b'Important'), (2, b'Normal')]),
        ),
    ]
