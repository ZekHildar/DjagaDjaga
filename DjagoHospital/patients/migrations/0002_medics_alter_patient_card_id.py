# Generated by Django 4.1.3 on 2022-12-13 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=50, verbose_name='Отчество')),
                ('category', models.CharField(max_length=50, verbose_name='Категория')),
                ('gender', models.CharField(max_length=1, verbose_name='Пол')),
                ('works_from', models.DateField(auto_now_add=True, verbose_name='Работает с')),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='card_id',
            field=models.SmallIntegerField(default=1, verbose_name='Номер карточки'),
        ),
    ]
