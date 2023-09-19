from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
        attrs={
            "class":"form-control",
            'placeholder':"Enter username",
        })
    )
    password = forms.CharField(
        widget=forms.TextInput(
        attrs={
            "class":"form-control",
            'placeholder':"Enter password",
        })
    )