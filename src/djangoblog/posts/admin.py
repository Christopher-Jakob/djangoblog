# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["title", "content"]

	class Meta:
		model = Post


admin.site.register(Post, PostAdmin)