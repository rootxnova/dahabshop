# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-21 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0009_post_title2'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='prics',
            field=models.CharField(default='', max_length=50),
        ),
    ]
