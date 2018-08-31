# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-28 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resdec', '0007_remove_variabilityenvironmentdata_relationship_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='variabilityenvironmentdata',
            name='user_column',
            field=models.CharField(blank=True, default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='variabilityenvironmentdata',
            name='feature_column',
            field=models.CharField(blank=True, default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='variabilityenvironmentdata',
            name='item_column',
            field=models.CharField(blank=True, default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='variabilityenvironmentdata',
            name='rating_column',
            field=models.CharField(blank=True, default=b'', max_length=20),
        ),
    ]