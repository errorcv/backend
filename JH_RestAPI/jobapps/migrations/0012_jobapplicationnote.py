# Generated by Django 2.1.5 on 2019-03-18 03:05

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('jobapps', '0011_auto_20190210_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplicationNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('job_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                               to='jobapps.JobApplication')),
            ],
        ),
    ]
