from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from patients.models import GroupType, Medics


class AddMedicForm(forms.ModelForm):
    class Meta:
     model = Medics
     fields = '__all__'
    # last_name = forms.CharField(label='Фамилия', max_length=50)
    # first_name = forms.CharField(label='Имя', max_length=50)
    # middle_name = forms.CharField(label='Отчество', max_length=50)
    # gender = forms.CharField(label='Пол', max_length=1)
    # birth_date = forms.DateField(label='Дата рождения')
    # works_from = forms.DateField(label='Работает с')
    # is_working = forms.BooleanField(label='Работает на данный момент')
    # grouptype = forms.ModelChoiceField(label='Категория', queryset=GroupType.objects.all(), empty_label='Не выбрана')
    # slug = forms.SlugField(label='URL', max_length=255)

class RegisterUserForm(UserCreationForm):
     username = forms.CharField(label='Логин')
     email = forms.EmailField(label='E-mail')
     password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
     password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())
     class Meta:
         model = User
         fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


