# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Business 

def business_create(request):
	context = {
	"title": "Create",
	}
	return render(request, "business_create.html", context)

def business_detail(request):
	context = {
	"title":"Detail",
	}
	return render(request, "business_detail.html", context)

def business_list(request):
	object_list = Business.objects.all()
	context = {
	"object_list": object_list,
	"title":"List",
	"user": request.user
	}
	return render(request, "business_list.html", context)

def business_update(request):
	context = {
	"title": "Update,"
	}
	return render(request, "business_update.html", context)

def business_delete(request):
	context = {
	"title": "Delete"
	}
	return render(request, "business_delete.html", context)

# Create your views here.
