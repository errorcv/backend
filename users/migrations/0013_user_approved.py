# Generated by Django 2.2 on 2019-05-02 00:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0012_profile_profile_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]