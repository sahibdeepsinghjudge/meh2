# Generated by Django 3.0.4 on 2021-09-10 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersData', '0016_auto_20210910_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationdata',
            name='location_sharing',
            field=models.CharField(choices=[('off', 'off'), ('on', 'on')], default='on', max_length=3),
        ),
    ]