# Generated by Django 5.0.6 on 2024-08-29 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0007_remove_enrollment_city_enrollment_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='City',
            new_name='city',
        ),
    ]
