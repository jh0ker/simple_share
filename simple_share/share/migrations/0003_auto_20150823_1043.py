# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_auto_20150823_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, auto_created=True),
        ),
    ]
