# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0003_auto_20150823_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
