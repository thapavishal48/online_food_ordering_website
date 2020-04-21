from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

from django import forms

class CustomUserCreationForm(UserCreationForm):     #it is make your own page for  ADD USER of admin page
    class Meta(UserCreationForm):
        model=CustomUser
        fields="__all__"

class CustomUserChangeForm(UserChangeForm):         #it is used to make edit page in admin page...Home › Userauth › Users › idea
    class Meta(UserChangeForm):
        model=CustomUser
        fields = "__all__"

class CustomUserUpdateForm(forms.ModelForm):            #it is used to update the user page
    class Meta:
        model=CustomUser
        fields=["first_name","last_name","email","location"]