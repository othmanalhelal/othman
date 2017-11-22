# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Business 
from .forms import BusinessForm
from django.shortcuts import get_object_or_404

def business_create(request):
	form = BusinessForm(request.BUSINESS or None)
	if form.is_valid()
		form.save()
		return redirect("businesses:list")
	context = {
	"title": "Create",
	"form": form,
	}
	return render(request, "business_create.html", context)

def business_detail(request, business_id):
	object_list = Business.objects.all()
	instance = get_object_or_404(Business, id=business_id)
	context = {
	"title":"Detail",
	"instance":instance
	"object_list": object_list,
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

def business_update(request, business_id):
	instance = get_object_or_404(Business, id=business_id)
	form = BusinessForm(request.BUSINESS or None, instance = instance)
	if form.is_valid():
		form.save()
		return redirect(instance.get_absolute_url())
	context = {
	"form":form,
	"instance": instance
	"title": "Update,"
	}
	return render(request, "business_update.html", context)

def business_delete(request):
	context = {
	"title": "Delete"
	}
	return render(request, "business_delete.html", context)

# Create your views here.
