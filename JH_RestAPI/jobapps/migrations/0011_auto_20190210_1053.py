# Generated by Django 2.1.5 on 2019-02-10 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapps', '0010_auto_20190210_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statushistory',
            old_name='application_status',
            new_name='applicationStatus',
        ),
    ]
