# Generated by Django 5.0.6 on 2024-08-29 14:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0006_alter_enrollment_city_alter_enrollment_invoice'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='city',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='City',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.city'),
        ),
    ]
