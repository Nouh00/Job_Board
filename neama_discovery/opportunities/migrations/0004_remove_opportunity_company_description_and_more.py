# Generated by Django 4.0.5 on 2022-06-13 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_rename_comapany_company'),
        ('opportunities', '0003_opportunity_applicants_alter_opportunity_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opportunity',
            name='company_description',
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='company_name',
        ),
        migrations.AddField(
            model_name='opportunity',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company', to='companies.company'),
        ),
    ]
