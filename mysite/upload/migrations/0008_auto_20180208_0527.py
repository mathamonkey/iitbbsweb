# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-08 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0007_auto_20180208_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='Author',
            field=models.CharField(default='Anonymus', max_length=30, null=True),
        ),
    ]
