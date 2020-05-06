# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-05 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0012_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='imageone',
        ),
        migrations.AddField(
            model_name='post',
            name='imagethree',
            field=models.ImageField(default='post_images/default.png', upload_to='post_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='imagetwo',
            field=models.ImageField(default='post_images/default.png', upload_to='post_images/'),
        ),
    ]
