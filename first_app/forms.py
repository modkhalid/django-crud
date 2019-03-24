from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model=User
        fields=['username','email','password']

class USerProfileForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=['profile_pic','portfolio_link']
