# Generated by Django 5.0.2 on 2024-03-04 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='job_title',
            field=models.CharField(choices=[('', ''), ('Admin', 'Admin'), ('Accountaint', 'Accountaint'), ('HR', 'HR'), ('Doctor', 'Doctor'), ('Nurse', 'Nurse'), ('Helper', 'Helper'), ('Cleaner', 'Cleaner'), ('technician', 'technician'), ('pharmacist', 'pharmacist'), ('therapist', 'therapist'), ('physician assistant', 'physician assistant'), ('Surgeon', 'Surgeon'), ('Receiption', 'Receiption'), ('Medical records clerk', 'Medical records clerk'), ('patient assignments', 'patient assignments')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='staff',
            name='sector',
            field=models.CharField(choices=[('', ''), ('Administrative sector', 'Administrative sector'), ('Service Sector', 'Service Sector')], default='', max_length=50),
        ),
    ]