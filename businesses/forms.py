from django import forms
from .models import Business

class BusinessForm(forms.ModelForm):
	class Meta:
		model = Business
		fields = ['title', 'content', 'image', 'draft', 'publish']

		widgets={
		'publish': forms.DateInput(attrs={"type":"date"}),
		}