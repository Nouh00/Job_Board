# Generated by Django 4.0.4 on 2022-05-27 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('opportunities', '0002_opportunity_user_applicant'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='applicants',
            field=models.ManyToManyField(null=True, through='opportunities.Applicant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
