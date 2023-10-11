from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from apps.models import Car
from django import forms

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'login_input2 pb-4'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'login_input2 pb-4'}))
    password2 = forms.CharField(label='Check password', widget=forms.PasswordInput(attrs={'class': 'login_input2 pb-4'}))

    class Meta: 
        model = User
        fields = ('username', 'password1', 'password2')