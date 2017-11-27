# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

class Business(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField(null=True, blank=True, upload_to="post_images")
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-timestamp", "-updated"]

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("businesses:detail", kwargs={"business_id": self.id})	

# Create your models here.
