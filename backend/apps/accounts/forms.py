

from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm ,PasswordChangeForm



class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        label="Электронная почта",
        widget=forms.EmailInput(attrs={"class":"form-control"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "type":"password",
                "autocomplete":"off",
                "placeholder":"Пароль"
            }
            )
    )


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": 'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class": 'form-control'}))

    username = forms.CharField(widget=forms.TextInput(attrs={"class": 'form-control'})
    )
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={"class": 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": 'form-control'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'phone'
        ]
