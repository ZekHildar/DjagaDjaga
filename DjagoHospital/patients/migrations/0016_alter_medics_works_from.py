# Generated by Django 4.1.3 on 2022-12-13 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0015_rename_is_workin_medics_is_working'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medics',
            name='works_from',
            field=models.DateField(verbose_name='Работает с'),
        ),
    ]
