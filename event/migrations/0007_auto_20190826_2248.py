# Generated by Django 2.2 on 2019-08-27 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_event_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]