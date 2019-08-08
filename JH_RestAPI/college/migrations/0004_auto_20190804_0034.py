# Generated by Django 2.2 on 2019-08-04 00:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('college', '0003_college_supported'),
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('supported', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='college',
            options={'ordering': ['name']},
        ),
    ]
