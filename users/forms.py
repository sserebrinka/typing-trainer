from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User  # Для редактирования данных пользователя
        fields = ['username', 'first_name', 'last_name', 'email']


class UserProfileExtraForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # Для редактирования данных из UserProfile
        fields = ['avatar']
