# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_auto_20161127_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleblock',
            name='location',
            field=models.CharField(default='aula 203', max_length=250),
            preserve_default=False,
        ),
    ]
