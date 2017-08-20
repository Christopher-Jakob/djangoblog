# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def posts_create(request):

	return HttpResponse("<h1>create</h1>")


def posts_detail(request): #retrieve

	return HttpResponse("<h1>detail</h1>")


def posts_list(request): #list items

	return HttpResponse("<h1>list</h1>")

def post_update(request):
	return HttpResponse("<h1>update</h1>")


def posts_delete(request): # delete

	return HttpResponse("<h1>delete</h1>")
