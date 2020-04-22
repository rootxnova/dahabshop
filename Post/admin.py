# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . models import Post,category
from django.contrib import admin

# Register your models here.
admin.site.register(Post)
admin.site.register(category)