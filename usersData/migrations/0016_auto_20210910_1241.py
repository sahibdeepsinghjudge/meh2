# Generated by Django 3.0.4 on 2021-09-10 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersData', '0015_auto_20210910_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationdata',
            name='date_up',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='locationdata',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]