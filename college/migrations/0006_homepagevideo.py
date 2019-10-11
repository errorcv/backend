# Generated by Django 2.2 on 2019-10-11 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_auto_20191011_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('embed_code', models.CharField(max_length=300)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('college', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='college.College')),
            ],
        ),
    ]
