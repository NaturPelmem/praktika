from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    last_name = forms.CharField(label='ФИО', widget=forms.TextInput(attrs={'placeholder': 'ФИО', 'name': 'txt'}))
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'placeholder': 'Логин', 'name': 'txt'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'name': 'pswd1'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль', 'name': 'pswd2'}))
    # is_superuser = forms.BooleanField(label='Король')
    # is_staff = forms.BooleanField(label='Царь')

    class Meta:
        model = User
        fields = ('last_name', 'username', 'password1', 'password2')
