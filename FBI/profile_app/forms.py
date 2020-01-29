from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    address = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    country = forms.CharField(max_length=20)
    city = forms.CharField(max_length=20)


    class Meta:
        model = User
        fields = [ 'username','first_name','last_name','email','phone','address','city','is_staff','country','password1','password2']


