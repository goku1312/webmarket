# Generated by Django 4.2.6 on 2023-11-09 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_templatecard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='password',
            new_name='state',
        ),
        migrations.RemoveField(
            model_name='register',
            name='otp_enabled',
        ),
        migrations.RemoveField(
            model_name='register',
            name='otp_secret',
        ),
    ]
