# Generated by Django 2.2 on 2019-04-26 11:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0004_employmentstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='emp_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    to='users.EmploymentStatus'),
        ),
    ]
