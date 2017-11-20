# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Business

class BusinessModelAdmin(admin.ModelAdmin):
	list_display = ["title", "timestamp", "updated"]
	list_filter = ["timestamp"]
	search_fields = ["title", "content"]
	list_display_links = ["timestamp"]
	list_editable = ["title"]
	class Meta:
		model = Business

admin.site.register(Business, BusinessModelAdmin)

# Register your models here.
