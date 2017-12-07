from django import forms
from .models import Business
from django.contrib.auth.models import User

class BusinessForm(forms.ModelForm):
	class Meta:
		model = Business
		fields = ['title', 'content', 'image', 'draft', 'publish']

		widgets={
		'publish': forms.DateInput(attrs={"type":"date"}),
		}

class UserSignup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

        widgets={
        'password': forms.PasswordInput(),
        }

class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())		