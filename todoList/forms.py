from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime

class TodoForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type":"text",
                "class":"form-control",
                'placeholder':"Enter task title",
            })
        )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":"form-control",
                "style":"height: 86px",
                'placeholder':"Enter task description",
            },
        ))
    dateTime = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={
                "class":"form-control",
                'type':'datetime-local',
                'placeholder':"Select date and time",
                'min':datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
            },
        ))
    completed = forms.BooleanField(
        required=False,
        initial=False,
        widget= forms.CheckboxInput(
            attrs={
                'class':"form-check-input",
                'style':"margin-left: 5px",
            },
            # choices=[True, False], 
        ))