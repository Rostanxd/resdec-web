# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-17 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resdec', '0011_auto_20180917_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=b'C:\\Users\\HP\\Documents\\Programming\\Python\\Repositorios\\resdec-web-master\\media/user_photos/'),
        ),
        migrations.AlterField(
            model_name='variabilityenvironmentdata',
            name='file',
            field=models.FileField(max_length=500, upload_to=b'C:\\Users\\HP\\Documents\\Programming\\Python\\Repositorios\\resdec-web-master\\media/user_data_uploaded/'),
        ),
    ]