# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170721_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='expire_date',
            field=models.DateTimeField(null=True),
        ),
    ]
