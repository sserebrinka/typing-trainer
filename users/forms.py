from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User  
        fields = ['username', 'first_name', 'last_name', 'email']


class UserProfileExtraForm(forms.ModelForm):
    class Meta:
        model = UserProfile 
        fields = ['avatar']
