# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-02-25 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_1', '0013_auto_20190225_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='User_type',
            field=models.IntegerField(),
        ),
    ]
