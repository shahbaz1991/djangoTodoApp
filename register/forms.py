from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import RegisterModel

class RegistrationForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
        attrs={
            "type":"text",
            "class":"form-control",
            'placeholder':"Enter full name",
        })
    )
    mobile = forms.IntegerField(
        widget=forms.TextInput(
        attrs={
            "type":"text",
            "class":"form-control",
            'placeholder':"Enter mobile number",
            'size':10
        })
    )
    email = forms.EmailField(
        widget=forms.TextInput(
        attrs={
            "class":"form-control",
            'placeholder':"Enter email",
        })
    )
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

    def clean_mobile(self):
        data = self.cleaned_data['mobile']
        mobileExist = RegisterModel.objects.filter(mobile = data)
        if (len(str(data)) < 10) or (len(str(data)) > 10):
            raise ValidationError(_('Mobile number should be 10 of digits'))
        elif (len(mobileExist) is not 0):
            raise ValidationError(_('Mobile already in use'))
        return data 
    
    def clean_username(self):
        data = self.cleaned_data['username']
        usernameExist = RegisterModel.objects.filter(username = data)
        if(len(usernameExist) is not 0):
            raise ValidationError(_('Username already taken'))
        return data