# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-08 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_file_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='Author',
            field=models.CharField(default='Anonymus', max_length=30),
        ),
    ]
