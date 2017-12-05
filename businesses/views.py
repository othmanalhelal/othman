# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Business 
from .forms import BusinessForm
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote
from django.http import Http404
from django.utils import timezone
from django.db.models import Q


def business_create(request):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    form = BusinessForm(request.BUSINESS or None)
    if form.is_valid():
        business = form.save(commit = False)
        business.author = request.user
        business.save()
        messages.success(requests, "Successfully Created!")
        return redirect("businesses:list")
    context = {
    "title": "Create",
    "form": form,
    }
    return render(request, "business_create.html", context)

def business_detail(request, business_slug):
    instance = get_object_or_404(Business, slug=business_slug)
    if instance.publish>timezone.now().date() or instance .draft:
        if not (request.user.is_staff or request.user.is_superuser):
            raise Http404
    context = {
    "title":"Detail",
    "instance":instance,
    "share_string": quote(instance.content)
    }
    return render(request, "business_detail.html", context)

def business_list(request):
    today = timezone.now().date()
    query = request.GET.get("q")
    if query:
        object_list = object_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(author__first_name__icontains=query)|
            Q(author__last_name__icontains=query)
            ).distinct()

    (draft=False).filter(publish__lte=today)
    if request.user.is_staff or request.user.is_superuser:
        object_list = Business.objects.all()

    query = request.GET.get("q")
    if query:
        object_list = object_list.filter(title__icontains=query)


    paginator = Paginator(object_list, 5) # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)
    context = {
    "object_list": object_list,
    "title":"List",
    "user": request.user,
    "today": today,
    }
    return render(request, "business_list.html", context)

def business_update(request, business_slug):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    instance = get_object_or_404(Business, slug=business_slug)
    form = BusinessForm(request.BUSINESS or None, instance = instance)
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully Edited!")
        return redirect(instance.get_absolute_url())
    context = {
    "form":form,
    "instance": instance,
    "title": "Update"
    }
    return render(request, "business_update.html", context)

def business_delete(request, business_slug):
    instance = get_object_or_404(Business, slug=business_slug)
    instance.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("businesses:list")

# Create your views here.
