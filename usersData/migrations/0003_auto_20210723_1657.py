# Generated by Django 3.0.4 on 2021-07-23 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersData', '0002_auto_20210723_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='bio',
            field=models.TextField(default='bio'),
        ),
    ]
