# Generated by Django 5.0.1 on 2024-04-20 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sca_app', '0004_alter_company_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='raitng',
            new_name='rating',
        ),
    ]