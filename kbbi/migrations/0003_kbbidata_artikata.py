# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-04 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbbi', '0002_auto_20170204_0508'),
    ]

    operations = [
        migrations.AddField(
            model_name='kbbidata',
            name='artikata',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]