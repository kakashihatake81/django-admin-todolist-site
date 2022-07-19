from django import forms
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class meta:
        model = User
        fields = ["username", "email", "password1", "password2"] #these 3 fields are already defined in python module usercreation form and email is already defined by us 
        