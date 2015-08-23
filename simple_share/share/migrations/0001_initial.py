# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=15)),
                ('note', models.CharField(max_length=250)),
                ('timestamp', models.DateTimeField()),
                ('path', models.CharField(max_length=255)),
            ],
        ),
    ]
