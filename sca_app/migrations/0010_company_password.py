# Generated by Django 5.0.3 on 2024-05-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sca_app', '0009_company_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='password',
            field=models.CharField(default='', max_length=32),
        ),
    ]
