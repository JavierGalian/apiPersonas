# Generated by Django 4.2.1 on 2023-05-07 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_remove_data_age_data_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='date_birth',
            field=models.DateField(default='2022-12-18'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='name_user',
            field=models.CharField(default='', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
