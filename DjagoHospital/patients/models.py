from django.db import models
from datetime import date

from django.urls import reverse


class Patient(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    middle_name = models.CharField(verbose_name='Отчество', max_length=50)
    gender = models.CharField(verbose_name='Пол', max_length=1)
    birth_date = models.DateField(verbose_name='Дата рождения', default=date(2000, 1, 1))
    card_id = models.SmallIntegerField(verbose_name='Номер карточки', default=1)
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Дата изменения', auto_now=True)
    disabled = models.BooleanField(verbose_name='Есть ли инвалидность', default=False)

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

class Medics(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    middle_name = models.CharField(verbose_name='Отчество', max_length=50)
    gender = models.CharField(verbose_name='Пол', max_length=1)
    birth_date = models.DateField(verbose_name='Дата рождения', default=date(2000, 1, 1))
    works_from = models.DateField(verbose_name='Работает с')
    is_working = models.BooleanField(verbose_name='Работает на данный момент', default=True)
    grouptype = models.ForeignKey('GroupType', on_delete=models.CASCADE, verbose_name='Категория')
    slug = models.SlugField(verbose_name='URL', max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('medic', kwargs={'med_slug': self.slug})



class GroupType(models.Model):
    grouptype = models.CharField(verbose_name="Категория", max_length=50)
    service = models.CharField(verbose_name="Оказываемая услуга", max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['grouptype']

    def __str__(self):
        return f'{self.grouptype} - {self.service}'





# Create your models here.
