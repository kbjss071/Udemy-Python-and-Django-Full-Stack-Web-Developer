from django import forms
from basic_app.models import UserProfileInfo
from django.contrib.auth.models import User

class UserProfileInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    portfolio = forms.URLField(required=False)
    picture = forms.ImageField(required=False)

    class Meta():
        Model = UserProfileInfo
        exclude = ('user',)