# Generated by Django 4.1.4 on 2022-12-11 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0016_alter_userprofile_phone_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('num', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=6)),
                ('reg_date', models.DateTimeField(auto_now=True)),
                ('approve', models.BooleanField(default=False)),
                ('car_type', models.CharField(choices=[('LI', 'Light'), ('S', 'Small'), ('SC', 'Subcompact'), ('C', 'Compact'), ('LA', 'Large'), ('SUV', 'SUV'), ('V', 'Van')], max_length=10)),
                ('entry_time', models.DateTimeField(auto_now=True)),
                ('exit_time', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.user')),
            ],
            options={
                'ordering': ['reg_date'],
            },
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.IntegerField(choices=[(101, '101동'), (102, '102동'), (103, '103동'), (104, '104동'), (105, '105동'), (106, '106동'), (107, '107동')], default='')),
                ('row', models.CharField(max_length=1)),
                ('column', models.IntegerField()),
                ('park_type', models.CharField(choices=[('G', 'General'), ('D', 'Disabled'), ('E', 'Electric')], max_length=8)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='park.car')),
            ],
            options={
                'ordering': ['row', 'column'],
            },
        ),
    ]