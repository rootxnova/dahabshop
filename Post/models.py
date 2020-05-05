# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

# Create your models here.


class category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name
class Post(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100, default='')
    prics = models.CharField(max_length=50, default='')
    location = models.CharField(max_length=50,default='')
    tags = TaggableManager()
    content = RichTextField()
    tafasel = models.TextField(default='')
    created = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(category)

    def __unicode__(self):
    	
		return self.title


	