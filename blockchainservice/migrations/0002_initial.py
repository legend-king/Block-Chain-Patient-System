# Generated by Django 4.1.7 on 2023-06-30 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        ('blockchainservice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientblockmodel',
            name='transactions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patientreport'),
        ),
    ]
