# Generated by Django 4.1.4 on 2022-12-22 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0020_medics_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='medics',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
