# Generated by Django 4.1.3 on 2022-12-13 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0014_medics_is_workin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medics',
            old_name='is_workin',
            new_name='is_working',
        ),
    ]