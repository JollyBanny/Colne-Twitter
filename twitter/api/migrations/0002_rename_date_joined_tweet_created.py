# Generated by Django 3.2 on 2021-04-22 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='date_joined',
            new_name='created',
        ),
    ]
