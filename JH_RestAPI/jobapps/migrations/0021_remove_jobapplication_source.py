# Generated by Django 2.2 on 2019-04-26 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapps', '0020_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='source',
        ),
    ]
