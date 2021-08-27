# Generated by Django 3.0.4 on 2021-07-24 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usersData', '0003_auto_20210723_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='socialAcc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.CharField(blank=True, max_length=255)),
                ('twitter', models.CharField(blank=True, max_length=255)),
                ('facebook', models.CharField(blank=True, max_length=255)),
                ('youtube', models.CharField(blank=True, max_length=455)),
                ('gmail', models.CharField(blank=True, max_length=255)),
                ('twitch', models.CharField(blank=True, max_length=255)),
                ('phone_no', models.IntegerField()),
                ('snapchat', models.CharField(blank=True, max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
