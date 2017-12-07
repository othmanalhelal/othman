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
from .forms import UserSignup, UserLogin
from django.contrib.auth import authenticate, login, logout


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
	if request.user.is_authenticated():
        if Like.objects.filter(post=instance, user=request.user).exists():
            liked = True
        else:
            liked = False
    business_like_count = instance.like_set.all().count()
	context = {
	"title":"Detail",
	"instance":instance,
	"share_string": quote(instance.content),
	"business_like_count":business_like_cout,
	"liked:liked,"
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

def ajax_like(request, post_id):
    business_object = Business.objects.get(id=business_id)
    new_like, created = Like.objects.get_or_create(user=request.user, business=business_object)

    if created:
        action="like"
    else:
        new_like.delete()
        action="unlike"

    business_like_count = business_object.like_set.all().count()
    response = {
        "action": action,
    }
    return JsonResponse(response, safe=False)	

def business_delete(request, business_slug):
	instance = get_object_or_404(Business, slug=business_slug)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect("businesses:list")

def usersignup(request):
    context = {}
    form = UserSignup()
    context['form'] = form
    if request.method == 'BUSINESS':
        form = UserSignup(request.BUSINESS)
        if form.is_valid():
            user = form.save()
            username = user.username
            password = user.password

            user.set_password(password)
            user.save()

            auth_user = authenticate(username=username, password=password)
            login(request, auth_user)

            return redirect("businesses:list")
        messages.error(request, form.errors)
        return redirect("posts:signup")
    return render(request, 'signup.html', context)

    def userlogin(request):
    context = {}
    form = UserLogin()
    context['form'] = form
    if request.method == 'BUSINESS':
        form = UserLogin(request.BUSINESS)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('businesses:list')

            messages.error(request, "Wrong username/password combination. Please try again.")
            return redirect("businesses:login")
        messages.error(request, form.errors)
        return redirect("businesses:login")
    return render(request, 'login.html', context)

    def userlogout(request):
    	logout(request)
    	return redirect("businesses:list")
	

# Create your views here.
