# Generated by Django 4.1.3 on 2022-12-05 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(default='', max_length=128, unique=True, verbose_name='닉네임'),
        ),
    ]
