# Generated by Django 5.0.6 on 2024-08-01 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquiries', '0008_enquiry_enrollment_fee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='enrollment_fee',
        ),
    ]
