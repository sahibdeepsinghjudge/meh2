# Generated by Django 3.0.4 on 2021-07-23 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_type', models.CharField(choices=[('Personal', 'Personal'), ('Business', 'Business')], max_length=10)),
                ('bio', models.TextField(blank=True, null=True)),
                ('dob', models.DateField()),
                ('security_q', models.CharField(max_length=255)),
                ('security_ans', models.CharField(max_length=255)),
                ('date_created', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
