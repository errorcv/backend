# Generated by Django 2.2 on 2019-08-21 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190821_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publisher_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]