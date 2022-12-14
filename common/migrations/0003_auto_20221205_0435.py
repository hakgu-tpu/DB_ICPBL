# Generated by Django 3.1.3 on 2022-12-04 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20221205_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
        migrations.AddField(
            model_name='user',
            name='user_building_num',
            field=models.IntegerField(default=0, max_length=16, verbose_name='동정보'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_first_name',
            field=models.CharField(default='', max_length=16, unique=True, verbose_name='성'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_house_num',
            field=models.IntegerField(default=0, max_length=8, verbose_name='호정보'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_last_name',
            field=models.CharField(default='', max_length=16, unique=True, verbose_name='이름'),
        ),
    ]
