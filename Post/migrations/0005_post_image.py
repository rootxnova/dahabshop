# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-15 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0004_auto_20200415_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='post_img/default.png', upload_to='post_img/'),
        ),
    ]