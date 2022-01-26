from dataclasses import field
import imp
from django import forms
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    class Meta:
        model=User
        fields=['username','password']

        
   

