# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . models import Post
from django.shortcuts import render
from taggit.models import Tag
from .forms import PostForm
from django.shortcuts import redirect



# Create your views here.

def all_categories(request):
	all_categories = Post.objects.filter(categories__name='home')
	context = {
		'all_categories' : all_categories
	}
	return render(request,'all_categories.html',context)


def all_clothes(request):
	all_categories = Post.objects.filter(categories__name='clothes')
	context = {
		'all_categories' : all_categories
	}
	return render(request,'all_clothes.html',context)

def all_electronics(request):
	all_categories = Post.objects.filter(categories__name='electronics')
	context = {
		'all_categories' : all_categories
	}
	return render(request,'all_electronics.html',context)

def all_houseware(request):
	all_categories = Post.objects.filter(categories__name='houseware')
	context = {
		'all_categories' : all_categories
	}
	return render(request,'all_houseware.html',context)

def post(request , id):
    post = Post.objects.get(id=id)
    common_tags = Post.tags.most_common()[:4]
    context = {
        'post' : post,
        'common_tags':common_tags
    }
    return render(request,'post.html',context)

def all_programming(request):
    all_categories = Post.objects.filter(categories__name='programming')
    context = {
        'all_categories':all_categories
    }
    return render(request,'all_programming.html',context)

def all_socialmedia(request):
    all_categories = Post.objects.filter(categories__name='socialmedia')
    context = {
        'all_categories':all_categories
    }
    return render(request,'all_socialmedia.html',context)

def add(request):
    all_categories = Post.objects.filter(categories__name='home')
    context = {
        'all_categories':all_categories
    }
    return render(request,'add.html',context)

def contact(request):
    context = {
        'contact':contact
    }
    return render(request,'contact.html',context)

def download(request):
    context = {
        'download':download
    }
    return render(request,'Download.html',context)

def statue(request):
    context={
        'statue' : statue
    }
    return render(request , 'statue.html' , context)

def charge(request):
    all_categories = Post.objects.filter(categories__name='Charge')
    context={
        'all_categories' : all_categories
    }
    return render(request , 'charge.html' , context)