# Generated by Django 2.2 on 2019-05-17 19:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0021_auto_20190511_2344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_photo',
            new_name='profile_photo_social',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_photo_custom',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
