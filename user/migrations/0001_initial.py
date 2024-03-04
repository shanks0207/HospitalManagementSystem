# Generated by Django 5.0.2 on 2024-03-02 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('doctor_id', models.CharField(max_length=10)),
                ('staff_id', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('birth_date', models.DateField()),
                ('email', models.CharField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=50)),
                ('full_address', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=20)),
            ],
        ),
    ]