# Generated by Django 3.0.4 on 2021-09-09 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersData', '0013_auto_20210909_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locationdata',
            old_name='latitiude',
            new_name='latitude',
        ),
    ]
