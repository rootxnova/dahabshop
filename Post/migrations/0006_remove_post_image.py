# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-15 18:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0005_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
