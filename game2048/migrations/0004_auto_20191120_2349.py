# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-20 15:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game2048', '0003_auto_20191108_0005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='top_ten',
            options={'ordering': ['result']},
        ),
    ]
