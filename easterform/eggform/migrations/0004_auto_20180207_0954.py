# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-07 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eggform', '0003_auto_20180207_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggs',
            name='number',
            field=models.CharField(max_length=10),
        ),
    ]
