# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-05 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emergency_contact', models.CharField(max_length=50)),
                ('QR_code', models.CharField(max_length=500)),
                ('Disability_status', models.BooleanField(default=False)),
                ('Height', models.FloatField()),
                ('weight', models.FloatField()),
                ('Blood_type', models.CharField(max_length=500)),
                ('Chronic_diseases', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='temp_register',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('home_phone_number', models.CharField(max_length=100)),
                ('work_phone_number', models.CharField(max_length=100)),
                ('Date_of_birth', models.DateField()),
                ('marital_status', models.CharField(max_length=100)),
                ('Child_num', models.CharField(max_length=100)),
                ('email_1', models.EmailField(max_length=100)),
                ('email_2', models.EmailField(max_length=100)),
                ('Nationality', models.CharField(max_length=100)),
                ('Profile_picture', models.ImageField(upload_to='')),
                ('Job_name', models.CharField(max_length=100)),
                ('Job_organization', models.CharField(max_length=100)),
                ('Jop_place', models.CharField(max_length=100)),
                ('Ssn', models.CharField(max_length=100)),
                ('Ssn_id', models.CharField(max_length=100)),
                ('New_Password', models.CharField(max_length=100)),
                ('SSN_Picture', models.ImageField(upload_to='')),
                ('User_type', models.IntegerField()),
                ('Create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='Patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.user'),
        ),
    ]