# Generated by Django 2.2 on 2019-08-04 02:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0024_profile_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='linkedin_info',
        ),
    ]
