# Generated by Django 5.0.6 on 2024-08-03 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquiries', '0022_enquiry_enrollment_fee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiry',
            old_name='qty_weeks',
            new_name='course_qty_weeks',
        ),
    ]
