# Generated by Django 2.2 on 2019-09-16 20:47
from django.core.files import File
from django.db import migrations
import uuid
from urllib.request import urlretrieve
from urllib.error import HTTPError
import os
from django.contrib.auth import get_user_model


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_delete_profile'),
    ]

    def move_data(apps, schema_editor):
        User = get_user_model()
        for user in User.objects.all():
            if not user.profile_photo_custom.name:
                if user.profile_photo_social is not None and user.profile_photo_social is not '':
                    try:
                        urlretrieve(user.profile_photo_social, filename=user.profile_photo_social.split('/')[-1])
                        file = open(user.profile_photo_social.split('/')[-1], 'rb')
                        filename = "%s.%s" % (uuid.uuid4(), 'jpg')
                        user.profile_photo_custom.save(filename, File(file), save=True)
                        os.remove(user.profile_photo_social.split('/')[-1])
                    except FileNotFoundError as err:
                        print(err)  # something wrong with local path
                    except HTTPError as err:
                        print(err)  # something wrong with url

    operations = [
        migrations.RunPython(move_data, reverse_code=migrations.RunPython.noop),
    ]
