# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-02-25 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_1', '0008_merge_20190225_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Profile_picture',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='SSN_Picture',
            field=models.FileField(upload_to=''),
        ),
    ]
