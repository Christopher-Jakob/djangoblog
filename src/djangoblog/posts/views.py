# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post

# Create your views here.

def posts_create(request):
	form = PostForm(request.Post or None) #doing it this way allows for modelForms validation!!
	if form.is_valid(): #again using the form validation and then actioning on it below!
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Sucessfully created!")
		return HttpResponseRedirect(instance.get_absolute_url())

	else:
		message.error(request, "Nope")
	"""if request.method == "POST":
			print request.POST.get("content")
			print request.POST.get("title")""" #not to be done this way, as it doesn't allow for form
					                                   #validate data!!
	context = {
	"form" : form,
	}
	return render(request,"post_form.html", context)


def posts_detail(request, pk=None): #retrieve
	instance = get_object_or_404(Post, id=id)
	context = {
	"title" : instance.title,
	"instance": instance
	}
	return HttpResponse("<h1>detail</h1>")



def posts_list(request, id=None):    #list items
	queryset = Post.objects.all()
	context = {
		"object_list": queryset,
		"title": "List"
	}
	return render(request,"post-list.html", context) #takes a request, the template, and context

def posts_update(request):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.Post or None, instnce = instance) 
	if form.is_valid(): 
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Sucessfully edited yo!", extra_tags='some-crazy-tag')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"title" : instance.title,
	"instance": instance,
	"form": form,
	}
	return render(request, "post_form.html", context)




def posts_delete(request): # delete
	instance = get_object_or_404(Post, id=id)
	instance.deleted()
	messages.success(request, "successfully deleted")
	return redirect("posts:list")
