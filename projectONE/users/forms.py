from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
"""
This file was made for the purpose of editting the form file that comes 
built in with the django framework. 
Here we needed a field that takes in an email account. 
and so it was added as below.
"""
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1' , 'password2']

"""
The class below is know as a model form. This alows the
ability to create a form that will work with a specific
model.
And the form below allows us to update our user model for the
purporse of the user updating their own profile.
"""
class UserUpdateForm(forms.ModelForm):
     email = forms.EmailField()

     class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']