# Generated by Django 3.0.4 on 2021-09-02 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usersData', '0007_otpmodule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='acc_type',
            field=models.CharField(choices=[('Personal', 'Personal'), ('Business', 'Business')], default='Personal', max_length=10),
        ),
        migrations.CreateModel(
            name='ProfileVisits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_hits', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_hit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileReactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.CharField(max_length=5)),
                ('reactor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactor', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
