# Generated by Django 2.0.5 on 2019-04-09 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_auto_20190410_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_medicine',
            name='med',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.all_medicine'),
        ),
        migrations.AlterField(
            model_name='patient_medicine',
            name='number_of_pills',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patient_medicine',
            name='number_of_potions',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patient_medicine',
            name='pat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
    ]
