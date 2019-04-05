# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-04 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App_1', '0002_auto_20190316_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_analytics',
            name='submit_analytics_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_medicine',
            name='submit_medicine_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_rays',
            name='submit_rays_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]