# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 23:23
from __future__ import unicode_literals

from django.db import migrations
import entries.models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_entry_extra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='extra',
            field=entries.models.JSONField(blank=True),
        ),
    ]