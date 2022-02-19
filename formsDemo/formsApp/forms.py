from django import forms
from django.forms import ModelForm


class UserRegistrationForm(forms.Form):
    GENDER = [('male', 'MALE'), ('female', 'FEMALE')]
    firstName = forms.CharField(required=False)
    lastName = forms.CharField()
    Email_ID = forms.CharField()
    Gender = forms.CharField(widget=forms.Select(choices=GENDER))
    password = forms.CharField(widget=forms.PasswordInput)
    ssn = forms.IntegerField()
