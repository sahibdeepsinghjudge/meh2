# Generated by Django 3.0.4 on 2021-08-16 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersData', '0005_auto_20210727_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialacc',
            name='discord',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='socialacc',
            name='telegram',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
