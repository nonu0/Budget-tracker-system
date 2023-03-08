from django import forms
from django.forms import  ModelForm
from budget.models import Owner
from .validators import password_validation
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Owner
        fields = ['first_name','last_name','username','owner','gender','phone_no','code','address','county','town']

    def clean_username(self):
        uname = self.cleaned_data.get('username').lower()
        if Owner.objects.filter(username__iexact=uname).exists():
            raise forms.ValidationError('Username already exists')
        return uname

    def clean_email(self):
        email = self.cleaned_data['owner'].lower()
        if Owner.objects.filter(owner=email).exists():
            raise forms.ValidationError('email has been taken')

        return email


class MyLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


