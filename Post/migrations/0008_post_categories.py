# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-17 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0007_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='Post.category'),
        ),
    ]
