# Generated by Django 5.0.6 on 2024-08-02 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiries', '0019_alter_enquiry_qty_weeks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='enrollment_fee',
            field=models.IntegerField(),
        ),
    ]
