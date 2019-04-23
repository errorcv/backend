# Generated by Django 2.2 on 2019-04-23 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20190423_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='downvote',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='upvote',
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_type', models.BooleanField(default=False)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
