# Generated by Django 4.0.5 on 2022-06-13 19:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comapany',
            new_name='Company',
        ),
    ]