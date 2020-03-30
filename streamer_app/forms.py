from django import forms
from django.contrib.auth.models import User
from .models import *

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'




