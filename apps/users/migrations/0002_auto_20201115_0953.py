# Generated by Django 2.2.1 on 2020-11-15 09:53

import apps.users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.users.models.upload_image_path),
        ),
        migrations.AlterField(
            model_name='organization',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.users.models.upload_image_path),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
