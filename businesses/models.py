# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Business(models.Model):
	author = models.ForeignKey(User, default=1)
	title = models.CharField(max_length=255)
	slug = models.SlugField(null=True)
	image = models.ImageField(null=True, blank=True, upload_to="business_images")
	content = models.TextField()
	draft = models.BooleanField(default=False)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-timestamp", "-updated"]

	class Like(models.Model):
    	user = models.ForeignKey(User)
    	post = models.ForeignKey(Post)
    	created = models.DateTimeField(auto_now_add=True)
    	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("businesses:detail", kwargs={"business_slug": self.slug})

def create_slug(instance, new_slug=None):
	slug = slugify (instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Business.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s"%(slug,qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_reciever(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug=create_slug(instance)

	pre_save.connect(pre_save_post_reciever,sender=Business)			

# Create your models here.
