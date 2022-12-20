from django import forms
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
