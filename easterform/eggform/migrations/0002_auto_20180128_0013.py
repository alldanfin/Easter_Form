# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-28 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eggform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggs',
            name='eggs',
            field=models.CharField(max_length=2),
        ),
    ]