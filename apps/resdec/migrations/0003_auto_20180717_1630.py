# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-17 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resdec', '0002_auto_20180716_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='variabilityenvironmentdata',
            name='status',
            field=models.CharField(choices=[(b'A', b'Active'), (b'I', b'Inactive')], default=b'', max_length=1),
        ),
        migrations.AlterField(
            model_name='variabilityenvironmentdata',
            name='file',
            field=models.FileField(upload_to=b'../static/data/uploaded'),
        ),
    ]
